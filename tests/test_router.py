import pytest
from pydantic import ValidationError

from agent_lab.router import RouteDecision, decide_route, handle


# Test whether the router identifies research requests.
def test_research_route():
    decision = decide_route("Find the latest AI research")

    assert decision.route == "research"
    assert decision.needs_tools is True


# Test whether the router identifies coding requests.
def test_coding_route():
    decision = decide_route("Help me debug Python code")

    assert decision.route == "coding"


# Test the default chat route.
def test_chat_route():
    decision = decide_route("Hello!")

    assert decision.route == "chat"
    assert decision.needs_tools is False


# Test whether Pydantic rejects unsupported routes.
def test_invalid_route():
    with pytest.raises(ValidationError):
        RouteDecision(
            route="delete",
            needs_tools=True,
            summary="Delete data"
        )


# Test whether the dispatcher selects the correct handler.
def test_dispatch():
    decision = decide_route("Hello!")
    result = handle(decision, "Hello!")

    assert result == "Chat handler: Hello!"
