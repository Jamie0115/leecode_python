import random


# 定義每張考卷的class
class TestScore:
    def __init__(self, number: int, score: int):
        self.number = number
        self.score = score


class ProjectScore:
    def __init__(self, project: str):
        self.project = project
        # 放TestScore的List
        self.scoreList = list()

    def addScore(self, t: TestScore):
        self.scoreList.append(t)

    def getAverageScore(self):
        totalScore = 0
        for o in self.scoreList:
            totalScore += o.score
        return totalScore / len(self.scoreList)


class ClassScore:
    def __init__(self, name: str):
        self.name = name
        self.projectDict = dict()

    def addProject(self, projectScore: ProjectScore):
        self.projectDict[projectScore.project] = projectScore


math = ProjectScore("Math")
for i in range(1, 41):
    math.addScore(TestScore(i, random.randint(1, 100)))

print(math.getAverageScore())

aClass = ClassScore("A")
aClass.addProject(math)



