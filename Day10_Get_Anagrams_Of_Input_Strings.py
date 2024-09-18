def group_Anagrams(strs):
    anagrams = {}
    for string in strs:
        key = ''.join(sorted(string))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(string)
    return list(anagrams.values())


strs = list(map(str, input().split()))
print(group_Anagrams(strs))
