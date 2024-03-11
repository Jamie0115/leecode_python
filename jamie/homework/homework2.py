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
        count = count_map.get(name, 0)
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


# 4. 哪個年齡層人數最多? => 20~24 , 25~29 , 30~34 , 35~39
def answer4(Student_list):
    age_range = {
        "person_20_24": 0,
        "person_25_29": 0,
        "person_30_34": 0,
        "person_35_39": 0
    }
    for item in Student_list:
        age = item.get("age")
        if age < 25:
            age_range["person_20_24"] += 1
        elif 25 <= age < 30:
            age_range["person_25_29"] += 1
        elif 30 <= age < 35:
            age_range["person_30_34"] += 1
        else:
            age_range["person_35_39"] += 1
    count_20_24 = int(age_range["person_20_24"])
    count_25_29 = int(age_range["person_25_29"])
    count_30_34 = int(age_range["person_30_34"])
    count_35_39 = int(age_range["person_35_39"])
    max(count_20_24, count_25_29, count_30_34, count_35_39)
    the_ages = []
    for key, value in age_range.items():
        if value == max(age_range.values()):
            the_ages.append(key)
    print("20~24: " + str(count_20_24))
    print("25~29: " + str(count_25_29))
    print("30~34: " + str(count_30_34))
    print("35~39: " + str(count_35_39))
    return the_ages, max(count_20_24, count_25_29, count_30_34, count_35_39)


# 5. 0分跟100分的人名
def answer5(Student_list):
    list_100 = list()
    list_0 = list()
    for item in Student_list:
        score = item.get("score")
        if score == 0:
            list_0.append(item.get("name")) # append =>是將元素加在串列最後面
        elif score == 100:
            list_100.append(item.get("name"))
    score_100 = "score 100: " + str(list_100)
    score_0 = "score 0: " + str(list_0)
    return score_100, score_0


# answer1
# print(answer1(Student_list))

# answer2
# print(answer2(Student_list))

# answer3
# print(answer3(Student_list))

# answer4
# print(answer4(Student_list))

# answer5
print(answer5(Student_list))

