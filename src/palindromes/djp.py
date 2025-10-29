"""
# palindromes

See https://github.com/terrycojones/palindromes
"""


def substrings(s, l):
    """
    generate length `l` substrings of `s`
    """
    for i in range(len(s) + 1 - l):
        yield s[i : i + l]


def djp_1(string):
    # ignore non alphabetic chars and case
    string = "".join(s for s in string.lower() if str.isalpha(s))

    string_rev = "".join(reversed(string))

    # check if substrings are in the reversed string
    # check longer substrings first
    for substring_length in reversed(range(1, len(string) + 1)):

        if palindromes := {
            substring
            for substring in set(substrings(string, substring_length))
            if substring in string_rev
        }:
            return palindromes

    return {""}
