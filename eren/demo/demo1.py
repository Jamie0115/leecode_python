import random


def getBoyNames():
    try:
        file1 = open("../../resource/boy.txt", "r", encoding="utf-8")
        content1 = file1.read()
        file1.close()
        return content1.split(",")
    except FileNotFoundError as e:
        print("File path is not found !!")


def getGirlNames():
    try:
        file2 = open("../../resource/girl.txt", "r", encoding="utf-8")
        content2 = file2.read()
        file2.close()
        return content2.split(",")
    except FileNotFoundError as e:
        print("File path is not found !!")


def randomName(array):
    index = random.randint(0, len(array) - 1)
    return array[index]


def randomHeight(input_sex):
    return round(random.uniform(160, 185), 1) if input_sex else round(random.uniform(150, 175), 1)


def randomWeight(input_sex):
    return round(random.uniform(60, 100), 1) if input_sex else round(random.uniform(45, 85), 1)


boyNames_array = getBoyNames()
girlNames_array = getGirlNames()

totalStudents = int(input("How many Students : "))
student_id = 0

student_list = []
while student_id < totalStudents:
    student_id += 1
    sex = random.randint(0, 1)

    student_list.append({
        "id": student_id,
        "sex": "M" if random.randint(0, 1) else "F",
        "name": randomName(boyNames_array if sex else girlNames_array),
        "age": random.randint(20, 39),
        "height": randomHeight(sex),
        "weight": randomWeight(sex),
        "score": random.randint(0, 100)
    })


try:
    file = open("../../resource/student_list.csv", "w", encoding="utf-8")
    content = "No.,Sex,Name,Age,Height,Weight,Score\n"
    for row in student_list:
        content += str(row["id"]) + ","
        content += row["sex"] + ","
        content += row["name"] + ","
        content += str(row["age"]) + ","
        content += str(row["height"]) + ","
        content += str(row["weight"]) + ","
        content += str(row["score"]) + "\n"

    file.write(content)
    file.close()
except FileNotFoundError as e:
    print("File path is not found !!")
