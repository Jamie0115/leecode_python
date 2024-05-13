"""
# 字串表示+練習
print("Hello, \nMr.White")
# 想印出 Hello " Mr.White ===> 在雙引號前面加一個\
print("Hello\" Mr.White")
Str1 = "Hello"
print(Str1 + " Mr.White")

# 函式 (function)
# 1. .lower() ==> 將每個字串字母變成小寫
Str1 = "Hello, Mr.White"
print(Str1.lower())
# 2. .upper() ==> 將每個字串字母變成大寫
Str1 = "Hello, Mr.White"
print(Str1.upper())
# 3. .isupper() ==> 判斷每個字串字母484大寫，不是就會回傳False，是就會回傳True
Str1 = "Hello, Mr.White"
print(Str1.isupper())
# 4. .islower() ==> 判斷每個字串字母484小寫，不是就會回傳False，是就會回傳True
Str1 = "Hello, Mr.White"
print(Str1.islower())

Str1 = "Hello, Mr.White"
print(Str1.lower().islower())
# 5. []==>第幾位是什麼字串
Str1 = "Hello, Mr.White"
print(Str1[5])
# 6. .index(" ")==>字串是第幾位
Str1 = "Hello, Mr.White"
print(Str1.index("l"))
# 7. .replace(" ")==>替換，將字串內的某個字替換成另一個字
Str1 = "Hello, Mr.White"
print(Str1.replace("l", "L"))


# stack() (堆疊) ===> 先進後出（First In Last Out）的資料結構，也就是最先進入的資料會先被取出
# append ===> 意思是向list中添加一個新元素

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
my_list = [1, 2, 3, 4, 5]
my_list.append(10)
print(my_list)
"""

"""
bracket = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
}
Left = "("
print(bracket[Left])
"""


def isValid(s):
    parens = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    stack = []
    for i in s:
        if i in parens:
            stack.append(i)
        elif len(stack) == 0 or parens[stack.pop()] != i:
            return False
    return len(stack) == 0
print(isValid(()))