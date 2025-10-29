import numpy as np
from math import ceil, floor
from typing import Iterable


def clean(s: str) -> str:
    return "".join(filter(str.isalpha, s.lower()))


def tj_1(s: str) -> set[str]:
    s = clean(s)
    s_len = len(s)
    max_len = 0
    palindromes = {""}

    for start_index in range(len(s)):
        # Small optimization: if there's not enough of 's' left for it to be possible to
        # find a new longest palindrome, we are done.
        if s_len - start_index < max_len:
            break

        first_letter = s[start_index]
        next_index = None

        while (next_index := s.rfind(first_letter, start_index, next_index)) != -1:
            candidate = s[start_index : next_index + 1]
            if candidate == candidate[::-1]:
                length = next_index - start_index + 1
                if length > max_len:
                    max_len = length
                    palindromes = {candidate}
                elif length == max_len:
                    palindromes.add(candidate)
                break

    return palindromes


def tj_2(s: str) -> set[str]:
    s = clean(s)
    s_len = len(s)

    def check_extremes(left: int, right: int) -> bool:
        return left >= 0 and right < s_len and s[left] == s[right]

    max_length = 0
    palindromes = {""}

    for index in np.arange(0.0, s_len - 0.5, 0.5):
        left = floor(index)
        right = ceil(index)
        radius = -1

        while check_extremes(left - (radius + 1), right + radius + 1):
            radius += 1

        if radius > -1:
            length = (radius << 1) + 2 - (left == right)
            palindrome = s[left - radius: right + radius + 1]
            if length > max_length:
                max_length = length
                palindromes = {palindrome}
            elif length == max_length:
                palindromes.add(palindrome)
            
    return palindromes


def tj_3(s: str) -> set[str]:
    s = clean(s)
    s_len = len(s)

    for length in range(s_len, 0, -1):
        palindromes = set()
        for start in range(0, s_len - length + 1):
            region = s[start: start + length]
            if region == region[::-1]:
                palindromes.add(region)
        if palindromes:
            return palindromes

    return {""}


def tj_4(s: str) -> set[str]:

    def substrings(s: str) -> Iterable[str]:
        for length in range(len(s), -1, -1):
            for start in range(0, len(s) - length + 1):
                yield s[start: start + length]

    def is_palindrome(p: str) -> bool:
        return len(p) < 2 or p[0] == p[-1] and is_palindrome(p[1:-1])

    def palindromes(s: str) -> Iterable[str]:
        length = -1
        for substring in filter(is_palindrome, substrings(s)):
            if length == -1:
                length = len(substring)
                yield substring
            elif len(substring) == length:
                yield substring
            else:
                break

    return set(palindromes(clean(s)))
