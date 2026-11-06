from agent_lab.router import decide_route, handle


def main():
    """
    Run an interactive command-line demo of the router.

    The program accepts user input, selects a route,
    displays the structured decision, and calls a handler.
    """
    print("Welcome to Agent Lab!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        decision = decide_route(user_input)

        print("\nRouter Decision:")
        print(decision.model_dump_json(indent=2))

        result = handle(decision, user_input)

        print("\nResult:")
        print(result)
        print()


if __name__ == "__main__":
    main()
