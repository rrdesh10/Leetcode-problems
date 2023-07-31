from collections import defaultdict


def valid_anagrama(s: str, t: str) -> bool:
    count = defaultdict(int)

    for i in s:
        count[i] += 1

    for i in t:
        count[i] -= 1

    for val in count.values():
        if val != 0:
            return False

    return True


valid_anagrama("anagrama", "nagarmaa")
