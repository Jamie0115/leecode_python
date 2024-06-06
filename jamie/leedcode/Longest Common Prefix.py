# strs[0] -> 這個array的第一個字串
# len(strs[0]) -> array第一個字串的長度
# len(strs) -> array字串裡面的長度
def longestCommonPrefix(strs) -> str:
    # Assumes the input list of strings is not empty
    # 假設輸入的字串為空字串輸出 -> " "
    # The outer loop goes through each character of the first string
    # 從第一個字串每個字符
    for i in range(len(strs[0])):
        # Inner loop checks the character at the current position across all other strings
        # 檢查除了第一個字串後的字符串在當前位置的字符
        for j in range(1, len(strs)):
            # Checks if we've reached the end of any string or a character mismatch is found
            # 檢查是否已經到達了任何字符串的末尾，或者找到了字符不匹配
            if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                # Return the longest common prefix found so far
                # 回傳最常相同的字串
                return strs[0][:i]
    # If no early return happened, the first string itself is the common prefix
    return strs[0]

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))