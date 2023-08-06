import collections


def lng_rpt_char(st: str, k: int) -> int:
    left = right = 0
    maxlen = 0
    count = collections.Counter()

    for right in range(1, len(st) + 1):
        count[st[right - 1]] += 1

        # find most char from left to right
        most = count.most_common()[0][1]

        # remain is no of chars to be replaced
        remain = right - left - most

        # num of char to replaced > then decrease window size
    if remain > k:
        count[st[left]] -= 1
        left = left + 1

    return max(right - left, maxlen)


lng_rpt_char("aabbcc", 3)
