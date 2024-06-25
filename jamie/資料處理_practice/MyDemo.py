from MyClass import TestScore


def read(path: str, folder: str, filename: str):
    with open(path + "/" + folder + "/" + filename + ".csv", 'r', encoding='utf-8') as f:
        content = f.read()
        return content.split("\n")


def write(path: str, folder: str, filename: str, lines: str):
    output = ""
    for line in lines:
        output += line + "\n"
    with open(path + "/" + folder + "/" + filename + ".csv", 'w', encoding='utf-8') as f:
        f.write(output)


projects = ["chinese", "english", "math"]
FILE_PATH = "./files"
all_class_score = list()
# for each 班級
for i in range(1, 17):
    classScoreDict = dict()
    # for each 科目
    for p in projects:
        rows = read(FILE_PATH, str(i), p)
        projectScoreList = list()
        # for each 每位同學
        for row in rows:
            column = row.split(",")
            if column[0] is not None and column[0].isdigit():
                # 創建物件TestScore塞入屬性
                myTestScore = TestScore(p, int(column[0]), int(column[1]))
                projectScoreList.append(myTestScore)
        classScoreDict[p] = projectScoreList
    all_class_score.append(classScoreDict)

print()
