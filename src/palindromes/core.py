import numpy as np
from math import ceil, floor


def clean(s: str) -> str:
    return "".join(filter(str.isalpha, s.lower()))


def p1(s: str) -> set[str]:
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


def p2(s: str) -> set[str]:
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
