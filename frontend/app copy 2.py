"""Simple dummy Python app for demonstration purposes."""

from datetime import datetime


def get_greeting(name: str) -> str:
    """Return a friendly greeting with the current timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, {name}! The time is {timestamp}."


def main() -> None:
    name = input("Enter your name: ") or "friend"
    print(get_greeting(name))


if __name__ == "__main__":
    main()
