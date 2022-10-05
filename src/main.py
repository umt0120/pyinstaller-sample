import os


def main() -> None:
    print(f"os.getcwd(): {os.getcwd()}")
    print(f"__file__: {__file__}")


if __name__ == "__main__":
    main()