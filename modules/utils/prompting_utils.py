# Prompt assembly for the NL to SPARQL
from modules.utils.domain import Domain
from prompt.prompts import (
    FEW_SHOT_EXAMPLES, _OUTPUT_FORMAT, _CONTEXT_HEADER, _COT_STEPS, _COT_OUTPUT_FORMAT,
)


# The KG schema (prefixes, classes, properties) injected into context-augmented styles.
def _kg_block() -> str:
    return f"=== KNOWLEDGE GRAPH CONTEXT ===\n{Domain}"


# Format the fixed few-shot exemplars (keyed by 'question') as an EXAMPLES block.
def _examples_block(examples: list) -> str:
    # One "Example N: Question / SPARQL" block per exemplar, numbered from 1.
    lines = [
        f"Example {i}:\nQuestion: {ex['question']}\nSPARQL:\n{ex['sparql']}"
        for i, ex in enumerate(examples, 1)
    ]
    return "=== EXAMPLES ===\n" + "\n\n".join(lines)


# Same as `_examples_block` but for DFSL-retrieved items.
def _examples_block_dynamic(examples: list) -> str:
    # Same layout as _examples_block, but the question text lives under 'label'.
    lines = [
        f"Example {i}:\nQuestion: {ex['label']}\nSPARQL:\n{ex['sparql']}"
        for i, ex in enumerate(examples, 1)
    ]
    return "=== EXAMPLES ===\n" + "\n\n".join(lines)


# Assemble the chat messages for one (style, question).
def build_prompt(style: str, question: str, retriever=None) -> list[dict]:
    tail = f"{_OUTPUT_FORMAT}\n\nQuestion: {question}"

    if style == "Zero-Shot":
        # No schema, no examples — just the instruction and the question.
        content = (
            "You are a SPARQL query generator.\n"
            "Convert the user's natural language question into a valid SPARQL query.\n\n"
            f"{tail}"
        )
    elif style == "Zero-Shot Context-Augmented":
        # Add the KG schema so the model knows the actual prefixes/properties.
        content = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{tail}"
    elif style == "Few-Shot Context-Augmented k=5":
        # Schema + a fixed set of 5 worked examples (same for every question).
        content = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{_examples_block(FEW_SHOT_EXAMPLES)}\n\n{tail}"
    elif style == "CoT Context-Augmented":
        # Schema + explicit reasoning steps; uses a different tail that asks the
        # model to reason first and then emit only the query.
        cot_tail = f"{_COT_OUTPUT_FORMAT}\n\nQuestion: {question}"
        content = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{_COT_STEPS}\n\n{cot_tail}"
    elif style == "DFSL":
        # Schema + exemplars retrieved per-question by embedding similarity.
        examples = retriever(question)
        content  = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{_examples_block_dynamic(examples)}\n\n{tail}"
    else:
        raise ValueError(f"Unknown prompt style: {style!r}")

    return [{"role": "user", "content": content}]


PROMPT_STYLES = [
    "Zero-Shot",
    "Zero-Shot Context-Augmented",
    "CoT Context-Augmented",
    "Few-Shot Context-Augmented k=5",
    "DFSL",
]