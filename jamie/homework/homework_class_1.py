"""
import abc

class Person(metaclass=abc.ABCMeta):
    __role = "Person"

    def __init__(self, name: str):
        self.__name = name

    def __printName(self):
        print("Hello, my name is " + self.__name + ".")

    @abc.abstractmethod
    def _printRole(self):
        return NotImplemented

    def introduce(self):
        self.__printName()
        self._printRole()


class Student(Person):
    __role = "Student"

    def __init__(self, name: str, number: int):
        super().__init__(name)
        self.number = number

    def _printRole(self):
        print("I am a {0}. My number is {1}.".format(self.__role, self.number))


class Teacher(Person):
    __role = "Teacher"

    def __init__(self, name: str, expertise: str):
        super().__init__(name)
        self.expertise = expertise

    def _printRole(self):
        print("I am a {0}. My specialize is {1}.".format(self.__role, self.expertise))

a = Teacher("Barry", "optical")
b = Student("Jamie", 1)

a.introduce()
b.introduce()
"""
# 學生
# 設計一個學生類別（Student），每個學生都有自己的學號（student_id）
# 、姓名（name）、年級（grade）、和科目成績（subject_scores），並提供以下功能：
# 新增一科成績（add_subject_score），可以新增一科科目的成績，包括科目名稱和成績。
# 查詢全部科目成績（get_all_subject_scores），可以獲取該學生的所有科目成績。
# 計算平均成績（calculate_average_score），可以計算該學生的平均成績。
# 獲取學生資訊（get_student_info），可以獲取該學生的所有資訊，包括學號、姓名、年級、科目成績和平均成績。

class Student:
    def __init__(self, studentID: int, name: str, grade: int, subjectScore: float):
        self.studentID = studentID
        self.name = name
        self.grade = grade
        self.__subjectScore = subjectScore

class SubjectScore:
    def __init__(self, subject: str, subjectScore: float):
        super().__init__(subjectScore)
        self.subject = subject
        self.scoreList = list()

    def addScore(self, t: Student):
        self.scoreList.append(t)

