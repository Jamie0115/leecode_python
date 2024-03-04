def data(array):
    data_content = "編號,姓名,年齡" + "\n"
    for item in array:
        data_content = data_content + item["No"] + "," + item["Name"] + "," + item["Age"] + "\n"
    return data_content


person_data = []
pass_name = "Momo"
No = 0
while True:
    name = input("Name: ")
    age = input("Age: ")
    No = No + 1

    if name == pass_name:
        print("Final")
        break
    person = {
        "No": str(No),
        "Name": name,
        "Age": age
    }
    person_data.append(person)

path = "C:/Users/funny/Documents/leecode_python/files/"
f = open(path + "demo.csv", "w", encoding="big5")  # 開檔, "w"是寫入模式
content = data(person_data)
f.write(content)
f.close()  # 關檔
