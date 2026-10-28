"""Which LLM account the agent and PDF ingest bill to: OpenRouter or Anthropic (direct API).

Switch (the choice is saved in runs/llm_provider.txt and used by every window until changed):
    python -m utils.llm_provider                  show the current account and whether each key is set
    python -m utils.llm_provider anthropic        use ANTHROPIC_API_KEY
    python -m utils.llm_provider openrouter       use OPENROUTER_API_KEY
    python -m utils.llm_provider test             one tiny request to the current account (fractions of a cent)
At the agent prompt type `provider`, `provider anthropic` or `provider openrouter`.
One run only: `python -m utils.pdf_ingest process --provider anthropic`; `start_batch.bat anthropic` saves the choice.

Order: --provider flag (this run) > saved choice > LLM_PROVIDER in .env > openrouter.
Model names stay in OpenRouter form everywhere (anthropic/claude-haiku-5.5). They are translated to Anthropic's form
(claude-haiku-5-5) only when a request goes to Anthropic, so only anthropic/* models work on the Anthropic account.
Anthropic is reached through its OpenAI-compatible endpoint, so callers keep using client.chat.completions.create.
Keys are read from .env and never printed, logged or passed to child processes.
"""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
CHOICE_PATH = BASE_DIR / "runs" / "llm_provider.txt"  # runs/ is gitignored

PROVIDERS = {
    "openrouter": {"label": "OpenRouter", "key": "OPENROUTER_API_KEY", "base_url": "https://openrouter.ai/api/v1"},
    "anthropic": {"label": "Anthropic", "key": "ANTHROPIC_API_KEY", "base_url": "https://api.anthropic.com/v1/"},
}
ALIASES = {"or": "openrouter", "open-router": "openrouter", "open_router": "openrouter",
           "claude": "anthropic", "anthropic-api": "anthropic", "direct": "anthropic"}
SECRET_ENV_KEYS = tuple(p["key"] for p in PROVIDERS.values())
DEFAULT = "openrouter"

_override = ""  # set by a --provider flag for this process only


def _load_env() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv(ENV_PATH)
    except ImportError:
        pass


def normalize(name: str) -> str:
    """Canonical provider name, or '' if unknown."""
    n = (name or "").strip().lower()
    n = ALIASES.get(n, n)
    return n if n in PROVIDERS else ""


def _saved() -> str:
    try:
        return normalize(CHOICE_PATH.read_text(encoding="utf-8"))
    except OSError:
        return ""


def current() -> str:
    _load_env()
    return normalize(_override) or _saved() or normalize(os.getenv("LLM_PROVIDER", "")) or DEFAULT


def label(name: str = "") -> str:
    return PROVIDERS[normalize(name) or current()]["label"]


def has_key(name: str = "") -> bool:
    _load_env()
    v = os.getenv(PROVIDERS[normalize(name) or current()]["key"], "")
    return bool(v) and not v.startswith("your_")


def use_for_this_run(name: str) -> str:
    """Override the provider in this process only (a --provider flag)."""
    global _override
    n = normalize(name)
    if not n:
        raise ValueError(f"Unknown provider '{name}'. Use one of: {', '.join(PROVIDERS)}.")
    _override = n
    return n


def set_provider(name: str) -> str:
    """Save the choice for every window and later runs (also clears a per-run override in this process)."""
    global _override
    n = normalize(name)
    if not n:
        raise ValueError(f"Unknown provider '{name}'. Use one of: {', '.join(PROVIDERS)}.")
    CHOICE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CHOICE_PATH.write_text(n + "\n", encoding="utf-8")
    _override = ""
    return n


def status_line(name: str = "") -> str:
    n = normalize(name) or current()
    return f"LLM account: {PROVIDERS[n]['label']} ({PROVIDERS[n]['key']} {'set' if has_key(n) else 'MISSING'})"


def api_model(model: str, name: str = "") -> str:
    """OpenRouter-style id -> the id this provider expects."""
    n = normalize(name) or current()
    if n != "anthropic":
        return model
    m = (model or "").strip()
    if m.startswith("anthropic/"):
        m = m[len("anthropic/"):]
    if "/" in m or ":" in m or not m.startswith("claude"):
        raise ValueError(f"Model '{model}' is not an Anthropic model, so it cannot run on the Anthropic account. "
                         "Use an anthropic/... model or switch back with `provider openrouter`.")
    return m.replace(".", "-")


def _plain_messages(messages):
    """Anthropic's compatible endpoint takes plain-string system messages; flatten OpenRouter cache_control parts."""
    out = []
    for msg in messages or []:
        content = msg.get("content") if isinstance(msg, dict) else None
        if isinstance(msg, dict) and msg.get("role") == "system" and isinstance(content, list):
            msg = dict(msg, content="\n\n".join(p.get("text", "") for p in content if isinstance(p, dict)))
        out.append(msg)
    return out


class _Completions:
    def __init__(self, inner, provider: str):
        self._inner, self._provider = inner, provider

    def create(self, *, model: str, messages=None, **kwargs):
        if self._provider == "anthropic":
            model = api_model(model, "anthropic")
            messages = _plain_messages(messages)
            kwargs.pop("extra_body", None)  # OpenRouter-only routing options
            kwargs.pop("temperature", None)  # current Claude models reject it on the direct API
        return self._inner.create(model=model, messages=messages, **kwargs)


class _Chat:
    def __init__(self, inner, provider: str):
        self.completions = _Completions(inner.completions, provider)


class LLMClient:
    """Thin wrapper around an OpenAI SDK client pointed at the chosen provider."""

    def __init__(self, provider: str):
        from openai import OpenAI
        cfg = PROVIDERS[provider]
        key = os.getenv(cfg["key"], "")
        if not key or key.startswith("your_"):
            raise RuntimeError(f"{cfg['key']} is not set. Add it to {ENV_PATH} (the {cfg['label']} account is selected).")
        self.provider = provider
        self.label = cfg["label"]
        self._client = OpenAI(base_url=cfg["base_url"], api_key=key)
        self.chat = _Chat(self._client.chat, provider)

    def __repr__(self):
        return f"<LLMClient {self.label}>"  # never shows the key


def make_client(name: str = "") -> LLMClient:
    _load_env()
    return LLMClient(normalize(name) or current())


def provider_of(client) -> str:
    return getattr(client, "provider", DEFAULT)


_PRICES = {}


def list_price_cost(model: str, tokens_in: int, tokens_out: int):
    """USD at list price (OpenRouter's public price list mirrors Anthropic's); None if unknown. Looked up once per model."""
    if model not in _PRICES:
        try:
            from utils import brain_enrich
            _PRICES[model] = brain_enrich._model_price(model)
        except Exception:
            _PRICES[model] = None
    price = _PRICES[model]
    return None if not price else tokens_in * price[0] + tokens_out * price[1]


def scrub_env(env: dict) -> dict:
    """Copy of env without any provider key (for child processes such as R or git)."""
    return {k: v for k, v in env.items() if not k.upper().startswith("OPENROUTER_") and k.upper() not in SECRET_ENV_KEYS}


def self_test(name: str = "") -> int:
    """One tiny request; reports OK or the error (never the key)."""
    n = normalize(name) or current()
    model = "anthropic/claude-haiku-4.5" if n == "openrouter" else "anthropic/claude-haiku-5.5"
    model = os.getenv("OPENROUTER_INGEST_MODEL") or model
    try:
        r = make_client(n).chat.completions.create(model=model, max_tokens=20,
                                                   messages=[{"role": "user", "content": "Reply with the single word OK."}])
        print(f"{PROVIDERS[n]['label']} works ({model} -> {api_model(model, n)}): {(r.choices[0].message.content or '').strip()[:40]}")
        return 0
    except Exception as e:
        msg = str(e)
        for k in SECRET_ENV_KEYS:
            v = os.getenv(k, "")
            if v:
                msg = msg.replace(v, "[key]")
        print(f"{PROVIDERS[n]['label']} test failed: {msg[:300]}")
        return 1


def main(argv: list = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args and args[0].lower() == "test":
        return self_test(args[1] if len(args) > 1 else "")
    if args:
        try:
            set_provider(args[0])
        except ValueError as e:
            print(e)
            return 2
        print(f"Saved. {status_line()}")
        print("A running agent window picks this up at the next request or ingest.")
    else:
        print(status_line())
        for n in PROVIDERS:
            print(f"   {n:<11} key {'set' if has_key(n) else 'missing'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
