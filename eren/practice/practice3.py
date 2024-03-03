# ord("a") = 97 => 字母轉換ASCII碼
# chr(97) = "a" => ASCII碼轉換字母
# A(65) ~ Z(90) a(97) ~ z(122)

string = input("Enter password:")
offset = 5

caesar_code = ""
for char in string:
    code = ord(char)  # ASCII code
    if 65 <= code <= 90:
        index = (code + offset - 65) % 26
        caesar_code += chr(index + 65)
    elif 97 <= code <= 122:
        index = (code + offset - 97) % 26
        caesar_code += chr(index + 97)
    else:
        caesar_code += char

print(caesar_code)
