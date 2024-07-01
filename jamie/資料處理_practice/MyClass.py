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

    def getAllScoreList(self):
        li = list()
        for o in self.scoreList:
            li.append(o.score)
        return li

    def getAverageScore(self):
        totalScore = sum(self.getAllScoreList())
        return totalScore / len(self.scoreList)

    def getMaxScore(self):
        return max(self.getAllScoreList())

    def getMinScore(self):
        return min(self.getAllScoreList())


class ClassScore:
    def __init__(self, name: str):
        self.name = name
        self.projectDict = dict()

    def addProject(self, projectScore: ProjectScore):
        self.projectDict[projectScore.project] = projectScore

    def getProjectAverageScore(self, project: str):
        projectScore = self.projectDict.get(project)
        return projectScore.getAverageScore() if projectScore is not None else 0
