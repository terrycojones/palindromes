def st_1(word):
    word = "".join([l for l in word if l.isalpha()]).lower()
    if not word:
        return {""}
    ps = list(set(word))

    for i, l in enumerate(word[1:], start=1):
        left = word[:i]
        right1 = word[i:]
        right2 = word[i + 1 :]

        hp1 = find_half_palindrome(left[::-1], right1)
        hp2 = find_half_palindrome(left[::-1], right2)

        cp = [hp1[::-1] + hp1, hp2[::-1] + l + hp2]
        cp = sorted(cp, key=len)[-1]  # can't have the same length

        if len(cp) == len(ps[0]) and cp not in ps:
            ps.append(cp)
        if len(cp) > len(ps[0]):
            ps = [cp]

    return set(ps)


def find_half_palindrome(rleft, right):
    if len(rleft) == 0 or len(right) == 0:
        return ""

    if rleft[0] == right[0]:
        return rleft[0] + find_half_palindrome(rleft[1:], right[1:])

    return ""
