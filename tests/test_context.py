from agent_lab.context import (
    ContextItem,
    clip,
    build_context,
)


def test_clip_short_text():
    """Short text should remain unchanged."""
    assert clip("Hello", 10) == "Hello"


def test_clip_long_text():
    """Long text should be truncated."""
    result = clip("Hello World", 5)

    assert result.startswith("Hello")
    assert "[truncated]" in result


def test_priority_order():
    """Higher-priority context should appear first."""
    items = [
        ContextItem("history", "Old messages", 1, 100),
        ContextItem("rules", "Follow instructions", 10, 100),
    ]

    result = build_context(items, total_limit=200)

    assert result.index("rules") < result.index("history")


def test_context_budget():
    """Final context must respect the total budget."""
    items = [
        ContextItem("history", "A" * 200, 1, 100),
        ContextItem("rules", "Important rules", 10, 100),
    ]

    result = build_context(items, total_limit=80)

    assert len(result) <= 80


def test_skip_large_block():
    """Skip an oversized block and check the next item."""
    items = [
        ContextItem("large", "A" * 100, 10, 100),
        ContextItem("small", "Hello", 1, 10),
    ]

    result = build_context(items, total_limit=50)

    assert "small" in result
    assert "large" not in result
