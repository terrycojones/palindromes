# This solution was written by Claude CLI when given the following prompt.
#
# Write a function that takes a string and returns a set of the longest palindromes
# found in the string. Note that the longest palindrome in "" is "". Put your function,
# named c_1 into a file called claude.py and import it into the test suite. Make sure
# the tests all pass. Use type hints. Do not look at any of the other solutions in the
# files in the src/palindromes directory!

def c_1(s: str) -> set[str]:
    """
    Returns a set of the longest palindromes found in the string.
    The function is case-insensitive and ignores non-alphanumeric characters.
    """
    # Clean the string: lowercase and keep only alphanumeric characters
    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    if not cleaned:
        return {""}

    # Find all palindromes using expand around center approach
    def expand_around_center(left: int, right: int) -> str:
        """Expand around the center and return the palindrome."""
        while left >= 0 and right < len(cleaned) and cleaned[left] == cleaned[right]:
            left -= 1
            right += 1
        return cleaned[left + 1:right]

    palindromes = set()
    max_length = 0

    for i in range(len(cleaned)):
        # Check for odd-length palindromes (center is a single character)
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > max_length:
            max_length = len(palindrome1)
            palindromes = {palindrome1}
        elif len(palindrome1) == max_length:
            palindromes.add(palindrome1)

        # Check for even-length palindromes (center is between two characters)
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > max_length:
            max_length = len(palindrome2)
            palindromes = {palindrome2}
        elif len(palindrome2) == max_length:
            palindromes.add(palindrome2)

    return palindromes
