def toContent(array):
    rtn_Content = "編號,姓名,年齡" + "\n"
    for item in array:
        rtn_Content = rtn_Content + item["no"] + "," + item["name"] + "," + item["age"] + "\n"
    return rtn_Content


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

path = "/Users/ericwu/Documents/workspace/demo/file/"
f = open(path + "demo.csv", "w", encoding="utf-8")  # 開檔, "w"是寫入模式
content = toContent(person_List)  # 呼叫 toContent 方法
f.write(content)
f.close()  # 關檔
