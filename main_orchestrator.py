import os
import json
import yaml
import subprocess
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Workspace data lives in fisheries_agent/ when this file sits above it.
ENV_PATH = Path(__file__).resolve().parent / ".env"
BASE_DIR = ENV_PATH.parent
if (BASE_DIR / "fisheries_agent").is_dir():
    BASE_DIR = BASE_DIR / "fisheries_agent"

load_dotenv(ENV_PATH)

_client = None

def get_client():
    """Creates the OpenRouter client on first use so a missing key gives a clear error."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or api_key.startswith("your_"):
            raise RuntimeError(
                f"OPENROUTER_API_KEY is not set. Add it to {ENV_PATH} (see .env.template)."
            )
        _client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    return _client

# Core Framework Constants
MANIFEST_PATH = BASE_DIR / "project_manifest.yaml"
BRAIN_SOURCES_DIR = BASE_DIR / "00_Fisheries_Brain" / "01_Sources"

def load_manifest():
    """Loads the scientist's specific RProject infrastructure map."""
    if not MANIFEST_PATH.exists():
        print("⚠️ Warning: project_manifest.yaml not found. Run setup_onboarding.py first.")
        return {}
    with open(MANIFEST_PATH, "r") as f:
        return yaml.safe_load(f)

# =====================================================================
# --- CORE TOOL SET 1: BASE SYSTEM & KNOWLEDGE TOOLS ---
# =====================================================================

def search_fisheries_brain(keyword: str):
    """Scans the Obsidian 01_Sources folder markdown files for literature context."""
    context_snippets = []
    if not BRAIN_SOURCES_DIR.exists():
        return "Fisheries brain sources directory missing."
        
    for md_file in BRAIN_SOURCES_DIR.glob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    context_snippets.append(f"--- Source: {md_file.name} ---\n{content[:1500]}\n")
        except Exception:
            continue
            
    if not context_snippets:
        return f"No direct matches found in literature for keyword: '{keyword}'."
    return "\n".join(context_snippets[:3])

def run_project_pipeline(project_name: str, script_name: str):
    """Executes an existing pipeline script inside a specific scientist's project directory."""
    manifest = load_manifest()
    project = manifest.get("projects", {}).get(project_name)
    
    if not project:
        return f"Error: Project '{project_name}' is not recognized in the system manifest."
        
    project_path = Path(project["project_path"])
    target_script = project_path / script_name
    
    if not target_script.exists():
        return f"Error: Script '{script_name}' not found at {target_script}"
        
    engine = "Rscript" if script_name.endswith(('.R', '.Rmd', '.qmd')) else "python"
    
    try:
        result = subprocess.run([engine, str(target_script)], capture_output=True, text=True, check=True)
        return f"Execution Successful!\nOutput:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Execution Failed!\nError:\n{e.stderr}\nOutput:\n{e.stdout}"

# =====================================================================
# --- CORE TOOL SET 2: SPECIALIZED AGENT MATH PIPELINES ---
# =====================================================================

def run_zero_inflated_model(csv_path: str, response_var: str, predictor_vars: list, zero_inflation_formula: str = "~1"):
    """Constructs and executes a safe glmmTMB R script dynamically for count data."""
    predictors_str = " + ".join(predictor_vars)
    r_script_content = f"""
    library(glmmTMB)
    data <- read.csv("{csv_path}")
    model <- glmmTMB({response_var} ~ {predictors_str}, ziformula = {zero_inflation_formula}, family = nbinom2, data = data)
    sink("tmb_model_output.txt")
    print(summary(model))
    cat("\\n--- CONFIDENCE INTERVALS ---\\n")
    print(confint(model))
    sink()
    """
    script_path = "temp_run_tmb.R"
    with open(script_path, "w") as f: 
        f.write(r_script_content)
    try:
        subprocess.run(["Rscript", script_path], capture_output=True, text=True, check=True)
        if os.path.exists("tmb_model_output.txt"):
            with open("tmb_model_output.txt", "r") as r: 
                return r.read()
        return "glmmTMB ran, but output log was missing."
    except subprocess.CalledProcessError as e: 
        return f"glmmTMB error: {e.stderr}"
    finally:
        if os.path.exists(script_path): 
            os.remove(script_path)

def run_nimble_mark_recapture(csv_path: str, capture_history_col: str, iterations: int = 10000):
    """Assembles and executes a standard population mark-resight model using NIMBLE in R."""
    r_script_content = f"""
    library(nimble)
    raw_data <- read.csv("{csv_path}")
    ch_matrix <- as.matrix(raw_data[, grepl("{capture_history_col}", colnames(raw_data))])
    n_ind <- nrow(ch_matrix)
    n_occasions <- ncol(ch_matrix)
    cjs_code <- nimbleCode({{
        for (i in 1:n_ind) {{
            for (t in (f[i]+1):n_occasions) {{
                z[i, t] ~ dbern(z[i, t-1] * phi)
                ch_matrix[i, t] ~ dbern(z[i, t] * p)
            }}
        }}
        phi ~ dunif(0, 1); p ~ dunif(0, 1)
    }})
    f <- apply(ch_matrix, 1, function(x) which(x == 1))
    constants <- list(n_ind = n_ind, n_occasions = n_occasions, f = f)
    data <- list(ch_matrix = ch_matrix)
    z_init <- matrix(1, nrow = n_ind, ncol = n_occasions)
    inits <- list(phi = 0.5, p = 0.5, z = z_init)
    nimble_mod <- nimbleModel(code = cjs_code, constants = constants, data = data, inits = inits)
    compiled_mod <- compileNimble(nimble_mod)
    mcmc_conf <- configureMCMC(nimble_mod, monitors = c('phi', 'p'))
    nimble_mcmc <- buildMCMC(mcmc_conf)
    compiled_mcmc <- compileNimble(nimble_mcmc, project = nimble_mod)
    samples <- runMCMC(compiled_mcmc, niter = {iterations}, nburnin = {int(iterations*0.1)})
    sink("nimble_mcmc_output.txt")
    print(summary(samples))
    sink()
    """
    script_path = "temp_run_nimble.R"
    with open(script_path, "w") as f: 
        f.write(r_script_content)
    try:
        subprocess.run(["Rscript", script_path], capture_output=True, text=True, check=True)
        if os.path.exists("nimble_mcmc_output.txt"):
            with open("nimble_mcmc_output.txt", "r") as r: 
                return r.read()
        return "NIMBLE ran, but summary log was missing."
    except subprocess.CalledProcessError as e: 
        return f"NIMBLE error: {e.stderr}"
    finally:
        if os.path.exists(script_path): 
            os.remove(script_path)

def run_multivariate_exploration(csv_path: str, method: str = "PCA"):
    """Automates multi-variate statistical graphics (PCA, MDS, Heatmaps) using R vegan."""
    r_script_content = f"""
    library(vegan)
    data <- read.csv("{csv_path}")
    num_idx <- sapply(data, is.numeric)
    numeric_data <- data[, num_idx]
    png("multivariate_plot.png", width=800, height=600)
    if ("{method.upper()}" == "PCA") {{
        biplot(rda(numeric_data, scale = TRUE), main="PCA Biplot")
    }} else if ("{method.upper()}" == "MDS") {{
        plot(metaMDS(vegdist(numeric_data, method="bray"), trace = FALSE), type="t", main="MDS Plot")
    }} else if ("{method.upper()}" == "HEATMAP") {{
        heatmap(as.matrix(numeric_data), main="Heatmap")
    }}
    dev.off()
    """
    script_path = "temp_explorer.R"
    with open(script_path, "w") as f: 
        f.write(r_script_content)
    try:
        subprocess.run(["Rscript", script_path], capture_output=True, text=True, check=True)
        return f"Successfully generated {method.upper()} plot saved to 'multivariate_plot.png'."
    except subprocess.CalledProcessError as e: 
        return f"Exploration failed: {e.stderr}"
    finally:
        if os.path.exists(script_path): 
            os.remove(script_path)

# =====================================================================
# --- OPENROUTER MASTER JSON SCHEMAS ---
# =====================================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_fisheries_brain",
            "description": "Searches Obsidian literature summaries for biological or methodology guidelines.",
            "parameters": {"type": "object", "properties": {"keyword": {"type": "string"}}, "required": ["keyword"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_project_pipeline",
            "description": "Runs an existing execution script inside one of the user's mapped RProjects.",
            "parameters": {
                "type": "object",
                "properties": {"project_name": {"type": "string"}, "script_name": {"type": "string"}},
                "required": ["project_name", "script_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_zero_inflated_model",
            "description": "Fits zero-inflated negative binomial models via glmmTMB.",
            "parameters": {
                "type": "object",
                "properties": {
                    "csv_path": {"type": "string"}, "response_var": {"type": "string"},
                    "predictor_vars": {"type": "array", "items": {"type": "string"}}, "zero_inflation_formula": {"type": "string"}
                },
                "required": ["csv_path", "response_var", "predictor_vars"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_nimble_mark_recapture",
            "description": "Launches a Bayesian NIMBLE MCMC analysis for tag resight metric histories.",
            "parameters": {
                "type": "object",
                "properties": {"csv_path": {"type": "string"}, "capture_history_col": {"type": "string"}, "iterations": {"type": "integer"}},
                "required": ["csv_path", "capture_history_col"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_multivariate_exploration",
            "description": "Generates PCA, MDS, or Heatmap biplots using R vegan.",
            "parameters": {
                "type": "object",
                "properties": {"csv_path": {"type": "string"}, "method": {"type": "string", "enum": ["PCA", "MDS", "HEATMAP"]}},
                "required": ["csv_path", "method"]
            }
        }
    }
]

available_functions = {
    "search_fisheries_brain": search_fisheries_brain,
    "run_project_pipeline": run_project_pipeline,
    "run_zero_inflated_model": run_zero_inflated_model,
    "run_nimble_mark_recapture": run_nimble_mark_recapture,
    "run_multivariate_exploration": run_multivariate_exploration
}

# =====================================================================
# --- ORCHESTRATION ENGINE LOOP ---
# =====================================================================

def ask_orchestrator(user_prompt: str, manifest: dict):
    manifest_context = yaml.dump(manifest, default_flow_style=False)
    
    system_prompt = f"""You are the Master Fisheries Orchestrator Agent. 
You run locally on this machine and manage a suite of specialized analysis tools and an Obsidian vault context window.
Maintain formatting and stylistic habits that mirror the scientist's noted documentation habits.

Here is the current scientist's machine layout and project structure configuration:
{manifest_context}"""

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

    client = get_client()
    response = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"🔄 Routing task to execution channel: {function_name}...")
            tool_output = function_to_call(**function_args)
            
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": tool_output,
            })
            
        second_response = client.chat.completions.create(
            model="anthropic/claude-3.5-sonnet",
            messages=messages,
        )
        return second_response.choices[0].message.content
        
    return response_message.content

if __name__ == "__main__":
    manifest = load_manifest()
    if not manifest:
        print("❌ Cannot start orchestrator without a valid project_manifest.yaml file.")
        exit(1)
        
    print("\n⚓ Master Fisheries Orchestrator Core Fully Loaded & Online ⚓")
    print("-----------------------------------------------------------------")
    
    while True:
        try:
            cmd = input("\n🐟 Master Command: ")
            if cmd.lower() == 'exit': 
                break
            if not cmd.strip(): 
                continue
            print(f"\n🤖 Agent Response:\n{ask_orchestrator(cmd, manifest)}")
        except KeyboardInterrupt:
            break
        except RuntimeError as e:
            print(f"❌ {e}")
