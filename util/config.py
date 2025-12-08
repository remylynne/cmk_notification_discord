import os



def context(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        raise KeyError(f"Environment variable '{key}' not found")
    return val

def parameter(key: str) -> str | None:
    raw = context("NOTIFY_PARAMETERS")
    for item in raw.split():
        if "=" in item:
            k, v = item.split("=", 1)
            if k == key:
                return v
    raise KeyError(f"key-value parameter '{key}' not found in NOTIFY_PARAMETERS")

icon = "https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/checkmk.svg"