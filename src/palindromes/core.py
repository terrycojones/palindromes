import re


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


def p3(s):
    s = re.sub(r"[^a-zA-Z]", "", s.lower())
    pals = set()
    length = len(s)
    for sublength in range(length, 0, -1):
        for offset in range(length - sublength + 1):
            ss = s[offset : offset + sublength]
            if ss == ss[::-1]:
                pals.add(ss)
        if pals:
            return pals
    return {""}


def p4(s):
    s = re.sub(r"[^a-zA-Z]", "", s.lower())
    length = len(s)
    seeds = {i: char for i, char in enumerate(s)}
    for offset in range(length - 1):
        if s[offset] == s[offset + 1]:
            seeds[offset] = s[offset : offset + 2]
    pals = {}
    max_len = 1
    for offset, seed in seeds.items():
        i = 1
        even = len(seed) - 1
        while (
            offset - i >= 0
            and offset + even + i < length
            and s[offset - i] == s[offset + even + i]
        ):
            seed = s[offset - i] + seed + s[offset + even + i]
            i += 1
        if len(seed) < max_len:
            continue
        if len(seed) > max_len:
            pals = {}
            max_len = len(seed)
        pals[offset] = seed
    if pals:
        return set(pals.values())
    return set("")
