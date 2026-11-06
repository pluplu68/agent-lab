from typing import Literal
from pydantic import BaseModel, ConfigDict

# Define the structured output format for routing decisions.
# Pydantic validates the fields and their data types.
class RouteDecision(BaseModel): 
    model_config = ConfigDict(extra="forbid")

    route: Literal["chat", "research", "coding"]
    needs_tools: bool
    summary: str


def decide_route(user_input: str) -> RouteDecision:
    """
    Classify the user's request and return a structured decision.

    This version uses keyword rules instead of an LLM.
    A later version will use an LLM for classification.
    """
    text = user_input.lower()

    if any(word in text for word in ["python", "code", "debug"]):
        return RouteDecision(
            route="coding",
            needs_tools=True,
            summary="The user needs coding assistance."
        )

    if any(word in text for word in ["research", "latest", "search"]):
        return RouteDecision(
            route="research",
            needs_tools=True,
            summary="The user needs research."
        )

    return RouteDecision(
        route="chat",
        needs_tools=False,
        summary="The user needs general assistance."
    )


def handle(decision: RouteDecision, user_input: str) -> str:
    """
    Dispatch the request to the handler selected by the router.

    The handlers are placeholders for future agent components.
    They do not call external tools or LLMs yet.
    """
    if decision.route == "chat":
        return f"Chat handler: {user_input}"

    if decision.route == "research":
        return f"Research handler: {user_input}"

    if decision.route == "coding":
        return f"Coding handler: {user_input}"

    raise ValueError("Unsupported route")
