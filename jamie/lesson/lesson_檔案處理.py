#  \n:換行  \t: TAB

path = "C:/Users/funny/Documents/leecode_python/files/"
f = open(path + "demo.txt", "w", encoding="utf-8")  # 開檔, "w"是寫入模式
content = "Hello" + "\n" + "World"
f.write(content)
f.close()  #關檔
"""

path = "C:/Users/funny/Documents/leecode_python/files/"
try:
    f = open(path + "demo.csv", "r", encoding="utf-8")  # 開檔, "r"是讀取模式
    content = f.read()
    f.close()  #關檔
    print(content)
except FileNotFoundError as e:
    print("File path is not found !!")
"""