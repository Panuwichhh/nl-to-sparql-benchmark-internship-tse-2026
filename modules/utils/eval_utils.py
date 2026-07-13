import re


def extract_sparql(text: str) -> str | None:
    """Recover a runnable query from raw model output."""
    if not text:
        return None
    t = text.strip()
    # strip CoT reasoning:
    delim = None
    for delim in re.finditer(r"(?i)SPARQL\s*:", t):
        pass
    if delim is not None:   
        t = t[delim.end():].strip()
    if "Cannot generate query" in t:
        return None
    # pull out ```...```
    m = re.search(r"```(?:sparql)?\s*(.*?)```", t, re.DOTALL | re.IGNORECASE)
    if m:
        t = m.group(1).strip()
    # keep only query
    m = re.search(r"(?is)\b(PREFIX|SELECT|ASK|CONSTRUCT)\b", t)
    if not m:
        return None
    t = t[m.start():].strip()
    return t or None
