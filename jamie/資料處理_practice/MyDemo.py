from MyClass import TestScore, ProjectScore, ClassScore

def read(path: str, folder: str, filename: str):
    with open(path + "/" + folder + "/" + filename + ".csv", 'r', encoding='utf-8-sig') as f:
        content = f.read()
        return content.split("\n")


def write(path: str, folder: str, filename: str, lines: str):
    output = ""
    for line in lines:
        output += line + "\n"
    with open(path + "/" + folder + "/" + filename + ".csv", 'w', encoding='utf-8-sig') as f:
        f.write(output)


def calculate_averages(class_scores):
    averages = list()

    for class_scores_dict in class_scores:
        class_average = dict()

        for project, scores in class_scores_dict.items():
            total_score = sum(test_score.score for test_score in scores)
            average_score = total_score / len(scores) if scores else 0
            class_average[project] = average_score

        averages.append(class_average)

    return averages


projects = ["chinese", "english", "math"]
FILE_PATH = "./files"
all_class_score = list()
# for each 班級
for i in range(1, 17):
    classScore = ClassScore(str(i))
    # for each 科目
    for p in projects:
        projectScore = ProjectScore(p)
        rows = read(FILE_PATH, str(i), p)
        # for each 每位同學
        for row in rows:
            column = row.split(",")
            if column[0] is not None and column[0].isdigit():
                # 創建物件TestScore塞入屬性
                projectScore.addScore(TestScore(int(column[0]), int(column[1])))
        classScore.addProject(projectScore)
    all_class_score.append(classScore)

# average = calculate_averages(all_class_score)
#
# # Print results
# for i, class_averages in enumerate(average, 1):
#     print(f"Class {i} averages:")
#     for projects, average in class_averages.items():
#         print(f"{projects}: {average:.2f}")
#     print()


# -------------------------------------------------------------------------
for classScore in all_class_score:
    if classScore.name == "1":
        projectScore = classScore.getProjectScore("math")
        print(projectScore)

