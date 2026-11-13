from dataclasses import dataclass
from typing import Iterable


@dataclass
class ContextItem:
    """
    Represent one piece of context from a specific source.
    """
    source: str
    content: str
    priority: int
    max_chars: int


def clip(text: str, limit: int) -> str:
    """
    Truncate text if it exceeds the character limit.
    """
    if len(text) <= limit:
        return text

    return text[:limit] + "\n...[truncated]"


def build_context(
    items: Iterable[ContextItem],
    total_limit: int
) -> str:
    """
    Build context from multiple sources.

    Steps:
    1. Sort items by priority.
    2. Truncate individual items.
    3. Check the total character budget.
    4. Return the selected context blocks.
    """

    # Higher-priority items are processed first.
    ordered = sorted(
        items,
        key=lambda x: x.priority,
        reverse=True
    )

    blocks = []
    used = 0

    for item in ordered:
        # Apply a character limit to this item.
        text = clip(item.content, item.max_chars)

        # Add the source label to the context block.
        block = f"\n## Source: {item.source}\n{text}\n"

        # Skip this block if it exceeds the remaining budget.
        if used + len(block) > total_limit:
            continue

        blocks.append(block)
        used += len(block)

    # Combine the selected blocks into one string.
    return "".join(blocks)