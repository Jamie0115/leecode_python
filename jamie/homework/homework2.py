"""
讀csv檔(student_list):
1. BMI過重的比例(>24) => %
2. 撞名最多次的名字 => 名字&次數
3. 男生vs女生，誰的平均分數比較高? => "M" , "F"
4. 哪個年齡層人數最多? => 20~24 , 25~29 , 30~34 , 35~39
5. 0分跟100分的人名 => [] , []
"""


def getStudentList():  #
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


# 1. BMI過重的比例(>24) => %
def answer1(Student_list):
    # BMI = 體重(公斤) / 身高2(公尺2)
    BMI_over = 0
    for item in Student_list:
        BMI = item["weight"] / (item["height"] / 100) ** 2
        # print(BMI)
        if BMI > 24:
            BMI_over = BMI_over + 1
    return BMI_over / len(Student_list)


# 2. 撞名最多次的名字 => 名字&次數
def answer2(Student_list):
    count_map = {}
    for item in Student_list:
        name = item.get("name")
        count = count_map.get(name)
        if count is None:
            count_map[item["name"]] = 1  # 如果這名字之前沒有出現過=1
        else:
            count_map[item["name"]] = count + 1
    the_names = []
    for key, value in count_map.items():
        if value == max(count_map.values()):
            the_names.append(key)
    return the_names, max(count_map.values())


# 3. 男生vs女生，誰的平均分數比較高?
def answer3(Student_list):
    girl_num = 0
    boy_num = 0
    girl_total_score = 0
    boy_total_score = 0
    for item in Student_list:
        sex = item["sex"]
        if sex == "F":
            girl_num += 1
            girl_total_score += item["score"]
        else:
            boy_num += 1
            boy_total_score += item["score"]
    girlScore = girl_total_score / girl_num
    boyScore = boy_total_score / boy_num
    print("Girl Score : " + str(girlScore))
    print("Boy Score : " + str(boyScore))
    return "Girl" if girlScore > boyScore else "Boy"


Student_list = getStudentList()

# answer1
# print(answer1(Student_list))

# answer2
# print(answer2(Student_list))

# answer3
# print(answer3(Student_list))
