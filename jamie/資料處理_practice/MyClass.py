class TestScore():
    def __init__(self, project: str, number: int, score: int):
        self.__project = project
        self.__number = number
        self.__score = score

    def getProject(self) -> str:
        return self.__project

    def getNumber(self) -> int:
        return self.__number

    def getScore(self) -> int:
        return self.__score


class ProjectScore:
    def __init__(self):
        self.scoreList = list()

    def addScore(self, testScore: TestScore):
        self.scoreList.append(TestScore)