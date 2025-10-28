def p1(s: str) -> set[str]:
    s = "".join(filter(str.isalpha, s.lower()))
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
    # s = s.replace(" ", "")
    return p1(s)
