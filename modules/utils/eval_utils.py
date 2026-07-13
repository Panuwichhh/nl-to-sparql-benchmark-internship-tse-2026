import re

# Extract sparql query from raw model output.
def extract_sparql(text: str) -> str | None:
    if not text:
        return None
    t = text.strip()

    # 1. Drop any chain-of-thought before the query: if the model wrote
    #    "SPARQL:" (possibly several times), keep only what follows the LAST one.
    delim = None
    for delim in re.finditer(r"(?i)SPARQL\s*:", t):
        pass
    if delim is not None:
        t = t[delim.end():].strip()

    # 2. Explicit refusal — no query to run.
    if "Cannot generate query" in t:
        return None

    # 3. Unwrap a ```sparql ... ``` (or plain ```) code fence if present.
    m = re.search(r"```(?:sparql)?\s*(.*?)```", t, re.DOTALL | re.IGNORECASE)
    if m:
        t = m.group(1).strip()

    # 4. Trim any leftover prose: start at the first real query keyword.
    #    No keyword found - the output isn't a query at all.
    m = re.search(r"(?is)\b(PREFIX|SELECT|ASK|CONSTRUCT)\b", t)
    if not m:
        return None
    t = t[m.start():].strip()
    return t or None
