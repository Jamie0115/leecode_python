def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return " "
    elif len(strs) == 1:
        return strs[0]
    else:
        tempString = strs[0]
        for i in range(1, len(strs)):
            currentString = strs[i]
            tempString = strs[i] if len(currentString) < len(tempString) else tempString
            tempSize = 0
            for word in range(len(tempString)):
                if tempString[word] == currentString[word]:
                    tempSize +=1
                else:
                    break
            tempString = tempString[:tempSize]
        return tempString


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
