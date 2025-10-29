import re

def nz_1(s):
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


def nz_2(s):
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
