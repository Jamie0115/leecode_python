import abc
class Person:
    def __init__(self, name: str):
        self._name = name  # protected

    def printName(self):

        print("My name is " + self._name + ".")

    @abc.abstractmethod
    def introduce(self):


class Student(Person):
    def __init__(self, name: str, number: int):
        super().__init__(name)
        self.number = number


class Teacher(Person):
    def __init__(self, name: str, expertise: str):
        super().__init__(name)
        self.expertise = expertise

    def printTeacherName(self):
        print(self._name + " is my " + self.expertise + " teacher.")

a = Student("Jamie", 1)
b = Teacher("Barry", "physics")

a.printName()
b.printTeacherName()