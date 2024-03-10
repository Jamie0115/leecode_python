"""
讀csv檔(student_list):
1. BMI過重的比例(>24) => %
2. 撞名最多次的名字 => 名字&次數
3. 男生vs女生，誰的平均分數比較高? => "M" , "F"
4. 哪個年齡層人數最多? => 20~24 , 25~29 , 30~34 , 35~39
5. 0分跟100分的人名 => [] , []
"""


def getStudentList():
    file = open("../../resource/student_list.csv", "r", encoding="big5")
    content = file.read()
    file.close()

    rows = content.split("\n")
    list = []
    for i in range(1, len(rows)):
        row = rows[i]
        if len(row) == 0:
            continue
        split_row = rows[i].split(",")

        list.append({
            "no": int(split_row[0]),
            "sex": split_row[1],
            "name": split_row[2],
            "age": int(split_row[3]),
            "height": float(split_row[4]),
            "weight": float(split_row[5]),
            "score": int(split_row[6])
        })
    return list


student_list = getStudentList()

# 2. 撞名最多次的名字 => 名字&次數

# 2-1. 先取得每個名字出現次數的dictionary
count_map = {}
for student in student_list:
    name = student.get("name")
    count = count_map.get(name, 0) + 1
    count_map[name] = count

# 2-2. 再從dictionary算出最大的次數
the_num = max(count_map.values())
the_names = []
for key, value in count_map.items():
    if value == the_num:
        the_names.append(key)
print(the_names)
print(the_num)

# 3. 男生vs女生，誰的平均分數比較高? => "M" , "F"
score_map = {
    "boy_num": 0,
    "girl_num": 0,
    "boy_total_score": 0,
    "girl_total_score": 0
}
for student in student_list:
    if student["sex"] == "M":
        score_map["boy_num"] += 1
        score_map["boy_total_score"] += student["score"]
    else:
        score_map["girl_num"] += 1
        score_map["girl_total_score"] += student["score"]

print(score_map["boy_total_score"] / score_map["boy_num"])
print(score_map["girl_total_score"] / score_map["girl_num"])
