"""
1. 讀csv檔，NO.,Name,Age
2. 計算所有人的平均年齡
3. print每個名字出現的次數
"""
"""
# "A,B,C".split(",") => ["A","B","C"]
str1 = input("Enter:")
arr = str1.split(', ')
print(arr)
"""
path = "C:/Users/funny/Documents/leecode_python/files/"
try:
    file = open(path + "demo.csv", "r", encoding="big5")  # 開檔, "r"是讀取模式
    content = file.read()
    file.close()  # 關檔
except FileNotFoundError as e:
    print("File path is not found !!")

rows = content.split("\n")
my_array = []  # 先統整出一個array，再從裡面整理各細項
for i in range(1, len(rows)):  # cancel掉第一行_No, Name, Age
    row = rows[i]
    if len(row) == 0:
        continue
    arr = row.split(',')
    print(arr)
    # 用dictionary呈現每個array中的細項，append是附加array的一個方法
    # eg.
    # list = [1,2,3,4,5,6]
    # list.append(10)
    # print(list)
    # [1, 2, 3, 4, 5, 6, 10]
    my_array.append({
        "no": arr[0],
        "name": arr[1],
        "age": int(arr[2])
    })
print(my_array)

total_age = 0
count_map = {}
for item in my_array:
    total_age = total_age + item["age"]
    name = item.get("name")
    count = count_map.get(name)
    if count is None:
        count_map[item["name"]] = 1  # 如果這名字之前沒有出現過=1
    else:
        count_map[item["name"]] = count+1  # 如果這名字之前有出現過+1
print(total_age)
print(total_age/len(my_array))
print(len(my_array))
print(count_map)


