# 把person_List => 欲輸出的csv 字串
def toContent(array):
    print(array)
    rtn_Content = "NO.,Name,Age" + "\n"
    for item in array:
        rtn_Content = rtn_Content + item["no"] + "," + item["name"] + "," + item["age"] + "\n"
    return rtn_Content

#1,Jamie,25\n2,Barry,30
# input = break
person_List = []
no = 0
while True:
    name = input("Enter your name : ")
    if name == "break":
        break
    age = input("Enter your age : ")

    no += 1
    person = {
        "no": str(no),
        "name": name,
        "age": age
    }
    person_List.append(person)

path = "/Users/ericwu/Documents/workspace/demo/files/"
f = open(path + "demo.csv", "w", encoding="utf-8")  # 開檔, "w"是寫入模式
content = toContent(person_List)  # 呼叫 toContent 方法
f.write(content)
f.close()  # 關檔
