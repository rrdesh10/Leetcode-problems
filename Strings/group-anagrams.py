from collections import defaultdict


def grp_anagrams(st) -> list:
    anagram_mp = defaultdict(list)
    for word in st:
        sorted_word = ''.join(sorted(word))
        anagram_mp[sorted_word].append(word)

    ans = [v for v in anagram_mp.values()]
    return ans


grp_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
