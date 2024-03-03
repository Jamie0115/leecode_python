"""
凱薩密碼是一個很有名的加密技術，就是把所有字母在字母表上往前或往後推移，這次就設定把所有字母往後推兩格
ex: a => c , B => D
"""

# ord("a") = 97 => 字母轉換ASCII碼
# chr(97) = "a" => ASCII碼轉換字母
# A(65) ~ Z(90) ; a(97) ~ z(122)

code = input("caesar_code:")
back = int(input("number:"))  # 字串要轉成整數 => str transfer int
sentence = ""

for word in code:
    password = ord(word)
    if password >= 65 and password <= 90:
        string = ( password - 65 + back) % 26
        sentence = sentence + chr(string + 65)
    elif password >= 97 and password <= 122:
        string = (password - 97 + back) % 26
        sentence = sentence + chr(string + 97)
    else:
        sentence = sentence + word

print(sentence)