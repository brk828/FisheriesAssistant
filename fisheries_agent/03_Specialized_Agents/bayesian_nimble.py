import os
import subprocess

def run_nimble_mark_recapture(csv_path: str, capture_history_col: str, iterations: int = 10000):
    """
    Assembles and executes a standard CJS or closed population mark-recapture 
    model using the NIMBLE engine in R.
    """
    r_script_content = f"""
    library(nimble)
    
    # Load raw data
    raw_data <- read.csv("{csv_path}")
    
    # Extract capture history matrix assuming standard comma format
    # In practice, the agent can expand this handling based on dataset
    ch_matrix <- as.matrix(raw_data[, grepl("{capture_history_col}", colnames(raw_data))])
    
    n_ind <- nrow(ch_matrix)
    n_occasions <- ncol(ch_matrix)
    
    # Define a classic State-Space Cormack-Jolly-Seber (CJS) model code block
    cjs_code <- nimbleCode({{
        for (i in 1:n_ind) {{
            # First capture is a given
            for (t in (f[i]+1):n_occasions) {{
                # State equation (Survival)
                z[i, t] ~ dbern(z[i, t-1] * phi)
                # Observation equation (Recapture)
                ch_matrix[i, t] ~ dbern(z[i, t] * p)
            }}
        }}
        # Priors
        phi ~ dunif(0, 1)
        p ~ dunif(0, 1)
    }})
    
    # Determine first capture occasion for each individual
    f <- apply(ch_matrix, 1, function(x) which(x == 1)[1])
    
    # Define data and constants for NIMBLE
    constants <- list(n_ind = n_ind, n_occasions = n_occasions, f = f)
    data <- list(ch_matrix = ch_matrix)
    
    # Basic initial values for latent states
    z_init <- matrix(1, nrow = n_ind, ncol = n_occasions)
    inits <- list(phi = 0.5, p = 0.5, z = z_init)
    
    # Build, compile, and run the MCMC
    print("Building NIMBLE model...")
    nimble_mod <- nimbleModel(code = cjs_code, constants = constants, data = data, inits = inits)
    compiled_mod <- compileNimble(nimble_mod)
    
    mcmc_conf <- configureMCMC(nimble_mod, monitors = c('phi', 'p'))
    nimble_mcmc <- buildMCMC(mcmc_conf)
    compiled_mcmc <- compileNimble(nimble_mcmc, project = nimble_mod)
    
    print("Running MCMC Chains...")
    samples <- runMCMC(compiled_mcmc, niter = {iterations}, nburnin = {int(iterations*0.1)})
    
    # Save output summaries
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
            with open("nimble_mcmc_output.txt", "r") as res_file:
                return res_file.read()
        return "NIMBLE executed, but summary log was not written."
    except subprocess.CalledProcessError as e:
        return f"NIMBLE execution failed:\n{e.stderr}"
    finally:
        if os.path.exists(script_path):
            os.remove(script_path)
