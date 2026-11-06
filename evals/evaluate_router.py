
import csv
import time
from pathlib import Path

from agent_lab.router import decide_route


def main():
    """
    Evaluate the router using 30 labeled requests.

    Metrics:
        - Route accuracy
        - False tool rate
        - Average latency
        - LLM API cost
    """

    # Load the evaluation dataset.
    data_path = Path(__file__).with_name("router_cases.csv")

    with data_path.open(encoding="utf-8", newline="") as file:
        cases = list(csv.DictReader(file))

    assert len(cases) == 30, "Expected 30 evaluation cases"

    correct_routes = 0
    false_tool_calls = 0
    no_tool_cases = 0
    total_latency_ms = 0.0
    errors = []

    # Evaluate each request independently.
    for case in cases:
        text = case["text"]
        expected_route = case["expected_route"]
        expected_tools = (
            case["expected_needs_tools"].lower() == "true"
        )

        # Measure the routing execution time.
        start = time.perf_counter()
        decision = decide_route(text)
        elapsed_ms = (time.perf_counter() - start) * 1000

        total_latency_ms += elapsed_ms

        # Check routing accuracy.
        if decision.route == expected_route:
            correct_routes += 1
        else:
            errors.append({
                "input": text,
                "expected": expected_route,
                "predicted": decision.route,
            })

        # Check unnecessary tool requests.
        if not expected_tools:
            no_tool_cases += 1
            if decision.needs_tools:
                false_tool_calls += 1

    # Calculate metrics.
    total = len(cases)

    route_accuracy = correct_routes / total
    false_tool_rate = (
        false_tool_calls / no_tool_cases
        if no_tool_cases else 0.0
    )
    avg_latency = total_latency_ms / total

    # The current router makes no paid LLM API calls.
    api_cost = 0.0

    print("\n=== Router Evaluation ===")
    print(f"Total Requests: {total}")
    print(f"Route Accuracy: {route_accuracy:.2%}")
    print(f"False Tool Rate: {false_tool_rate:.2%}")
    print(f"Average Latency: {avg_latency:.4f} ms")
    print(f"LLM API Cost: ${api_cost:.4f}")

    # Show incorrect routing decisions.
    print("\n=== Misclassified Requests ===")
    for error in errors:
        print(f"\nInput: {error['input']}")
        print(f"Expected: {error['expected']}")
        print(f"Predicted: {error['predicted']}")


if __name__ == "__main__":
    main()