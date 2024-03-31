"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        isJump = False
        for i in range(len(s)):
            if isJump:
                isJump = False
                continue

            if i != len(s) - 1 and s[i] in ["I", "X", "C"]:
                if s[i] == "I" and s[i + 1] == "V":
                    num += 4
                    isJump = True
                elif s[i] == "I" and s[i + 1] == "X":
                    num += 9
                    isJump = True
                elif s[i] == "X" and s[i + 1] == "L":
                    num += 40
                    isJump = True
                elif s[i] == "X" and s[i + 1] == "C":
                    num += 90
                    isJump = True
                elif s[i] == "C" and s[i + 1] == "D":
                    num += 400
                    isJump = True
                elif s[i] == "C" and s[i + 1] == "M":
                    num += 900
                    isJump = True
                else:
                    num += symbol_dict.get(s[i])
            else:
                num += symbol_dict.get(s[i])
        return num


solution = Solution()
print(solution.romanToInt(input("Input:")))
