# ----------------------------------------------------------------

# ord(c) :  傳回字元c的編碼
print("ord('a'):", ord('a'))

# chr(i) : 傳回編碼為i的字元
print("chr(97):", chr(97))

# len(s) : 傳回字串s的長度
print("len('abc'):", len('abc'))

# str(n) : 將數值n轉換成字串
print("str(n):", str(97))

# ----------------------------------------------------------------

# s1 + s2 : 字串s1和s2連接
print("'s1'+'s2':", 's1' + 's2')

# s1 * n : 字串s1重複n次
print("'s1'*3:", 's1' * 3)

# s1[n] : 提取字串s1的第n個字元(從0開始)
print("'abc'[1]:", 'abc'[1])

# s1[start:end] : 提取字串s1的start到end-1的字元
print("'abcde'[3:5]:", 'abcde'[2:5])

# ----------------------------------------------------------------

# s.upper() ; s.lower() : 字串s全部轉大寫/小寫
print("'abCDe'.upper():", 'abCDe'.upper())
print("'ABcdE'.lower():", 'ABCDE'.lower())

# s.swapcase() : 字串s的大小寫互換
print("'aBcDe'.swapcase():", 'aBcDe'.swapcase())

# s.capitalize() : 字串s的第一個字母大寫
print("'eren'.capitalize():", 'eren'.capitalize())

# s.title() : 字串s裡，每一個單字的第一個字母大寫
print("'eren yaeger'.title():", 'eren yaeger'.title())

# ----------------------------------------------------------------

# s1 in s2 , s1 not in s2 : 檢查字串s1是否在字串s2內
print("'a' in 'abc':", 'a' in 'abc')
print("'a' not in 'abc':", 'a' not in 'abc')

# s.isupper() ; s.islower() : 檢查字串s是否都為大寫/小寫
print("'abcde'.isupper():", 'abcde'.isupper())
print("'abcde'.islower():", 'abcde'.islower())

# s.startswith(s1) ; s.endswith(s1) : 檢查字串s是否以字串s1開頭/結尾
print("'abcde'.startswith('ab'):", 'abcde'.startswith('ab'))
print("'abcde'.endswith('ab'):", 'abcde'.endswith('ab'))

# s.isalpha() : 檢查字串s是否都是英文字母
print("'abcde'.isalpha():", 'abcde'.isalpha())

# s.isdigit() : 檢查字串s是否都是數字
print("'12345'.isdigit():", '12345'.isdigit())

# s.isalnum() : 檢查字串s是否都是英文字母或數字
print("'abc12'.isalnum():", 'abc12'.isalnum())

# s.isspace() : 檢查字串s是否都是空格
print("'     '.isspace():", '     '.isspace())

# ----------------------------------------------------------------

# s1.count(s) : 計算s在s1中出現的次數
print("'ababa'.count('a'):", 'ababa'.count('a'))

# s1.find(s) : 找出s在s1中，首次出現的位置
print("'ababa'.find('b'):", 'ababa'.find('b'))

# s1.rfind(s) : 找出s在s1中，最後出現的位置
print("'ababa'.rfind('b'):", 'ababa'.rfind('b'))

# ----------------------------------------------------------------

# s.replace(old, new) : 將字串s中，old的部分替換成new
print("'abc ab'.replace('ab', 'xy'):", 'abc ab'.replace('ab', 'xy'))

# s.join([s1,s2,...,sn]) : 將字串s1,s2,...,sn用字串s串起來
print("'&'.join(['a', 'b', 'c', 'd', 'e']):", '&'.join(['a', 'b', 'c', 'd', 'e']))

# s.lsplit(chars) ; s.rsplit(chars) : 從s的左側/右側刪除chars所指定的字元，直到不是指定字元為止
print("'aaabccc'.lstrip('a'):", 'aaabccc'.lstrip('a'))
print("'aaabccc'.rstrip('c'):", 'aaabccc'.rstrip('c'))

# ----------------------------------------------------------------