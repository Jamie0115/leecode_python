from functools import reduce


# 學生
# 設計一個學生類別（Student），每個學生都有自己的學號（student_id）
# 、姓名（name）、年級（grade）、和科目成績（subject_scores），並提供以下功能：
# 新增一科成績（add_subject_score），可以新增一科科目的成績，包括科目名稱和成績。
# 查詢全部科目成績（get_all_subject_scores），可以獲取該學生的所有科目成績。
# 計算平均成績（calculate_average_score），可以計算該學生的平均成績。
# 獲取學生資訊（get_student_info），可以獲取該學生的所有資訊，包括學號、姓名、年級、科目成績和平均成績。
class Subject:
    def __init__(self, name: str, score: float):
        self.__name = name
        self.__score = score

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score


class Student:
    def __init__(self, sid: int, name: str, grade: int):
        self.__sid = sid
        self.__name = name
        self.__grade = grade
        self.__subjectScoreDict = dict()

    def add_subject_score(self, subject: Subject) -> None:
        self.__subjectScoreDict[subject.getName()] = subject

    def get_all_subject_scores(self) -> list:
        returnList = list()
        for subject in self.__subjectScoreDict.values():
            returnList.append(subject.getName() + ":" + str(subject.getScore()))
        return returnList

    def calculate_average_score(self) -> float:
        allSubject = self.__subjectScoreDict.values()
        total = reduce(lambda x, y: x.getScore() + y.getScore(), allSubject)
        return total / len(self.__subjectScoreDict)

    def get_student_info(self) -> dict:
        return {
            "sid": self.__sid,
            "name": self.__name,
            "grade": self.__grade,
            "subject_score": self.get_all_subject_scores(),
            "average_score": self.calculate_average_score()
        }


a = Student(1, "Eren", 3)
a.add_subject_score(Subject("Math", 90.5))
a.add_subject_score(Subject("English", 60.5))

print(a.get_student_info())
