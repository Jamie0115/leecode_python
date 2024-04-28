def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    for s in strs[1:]:
        print(s)

    return strs


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
