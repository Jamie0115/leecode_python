import abc


class Person(metaclass=abc.ABCMeta):
    __role = "Person"

    def __init__(self, name: str):
        self.__name = name

    def introduce(self):
        self._printRole()
        self.__printName()

    @abc.abstractmethod
    def _printRole(self):
        return NotImplemented

    def __printName(self):
        print("My name is " + self.__name)


class Student(Person):
    __role = "Student"

    def __init__(self, name: str, number: int):
        super().__init__(name)
        self.__number = number

    def _printRole(self):
        print("Hey, I am a " + self.__role)
        print("My number is " + str(self.__number))


class Teacher(Person):
    __role = "Teacher"

    def __init__(self, name: str, expertise: str):
        super().__init__(name)
        self.__expertise = expertise

    def _printRole(self):
        print("Hello, I am a " + self.__role)
        print("My expertise is " + self.__expertise)


a = Student("Eren", 1)
b = Teacher("Andy", "Math")

a.introduce()
b.introduce()
