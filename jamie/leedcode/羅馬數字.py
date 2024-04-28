"""
    Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
def romanToInt(s):  # 先列出來個羅馬數值代表的數字
    roman_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    for i in range(len(s) - 1):
        print(i)
        if roman_dic[s[i]] < roman_dic[s[i + 1]]:  # 發現特例，像是IV = 4、VX = 5、XL = 40、LC = 50 ...
            result = result - roman_dic[s[i]]
        else:
            result = result + roman_dic[s[i]]
    result = result + roman_dic[s[-1]]  # 要記得走訪完最後一個
    return result
print(romanToInt("LXIII"))