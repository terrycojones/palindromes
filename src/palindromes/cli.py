import argparse
from palindromes.core import p1


def main() -> None:
    """Command-line interface for finding palindromes in a string."""
    parser = argparse.ArgumentParser(
        description="Find the longest palindromes in a string"
    )
    parser.add_argument(
        "text", type=str, nargs="+", help="The string to search for palindromes"
    )

    args = parser.parse_args()

    palindromes: set[str] = p1("".join(args.text))
    n = len(palindromes)
    length = len(list(palindromes)[0])

    print(
        f"Found {n} palindrome{'' if n == 1 else 's'} of length {length}:",
        ", ".join(sorted(palindromes)),
    )


if __name__ == "__main__":
    main()
