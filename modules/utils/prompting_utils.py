"""Prompt assembly for the NL to SPARQL"""
from modules.utils.domain import Domain
from prompt.prompts import (
    FEW_SHOT_EXAMPLES, _OUTPUT_FORMAT, _CONTEXT_HEADER, _COT_STEPS, _COT_OUTPUT_FORMAT,
)


def _kg_block() -> str:
    return f"=== KNOWLEDGE GRAPH CONTEXT ===\n{Domain}"


def _examples_block(examples: list) -> str:
    lines = [
        f"Example {i}:\nQuestion: {ex['question']}\nSPARQL:\n{ex['sparql']}"
        for i, ex in enumerate(examples, 1)
    ]
    return "=== EXAMPLES ===\n" + "\n\n".join(lines)


def _examples_block_dynamic(examples: list) -> str:
    lines = [
        f"Example {i}:\nQuestion: {ex['label']}\nSPARQL:\n{ex['sparql']}"
        for i, ex in enumerate(examples, 1)
    ]
    return "=== EXAMPLES ===\n" + "\n\n".join(lines)


def build_prompt(style: str, question: str, retriever=None) -> list[dict]:
    tail = f"{_OUTPUT_FORMAT}\n\nQuestion: {question}"

    if style == "Zero-Shot":
        content = (
            "You are a SPARQL query generator.\n"
            "Convert the user's natural language question into a valid SPARQL query.\n\n"
            f"{tail}"
        )
    elif style == "Zero-Shot Context-Augmented":
        content = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{tail}"
    elif style == "Few-Shot Context-Augmented k=5":
        content = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{_examples_block(FEW_SHOT_EXAMPLES)}\n\n{tail}"
    elif style == "CoT Context-Augmented":
        cot_tail = f"{_COT_OUTPUT_FORMAT}\n\nQuestion: {question}"
        content = f"{_CONTEXT_HEADER}\n\n{_kg_block()}\n\n{_COT_STEPS}\n\n{cot_tail}"
    elif style == "DFSL":
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