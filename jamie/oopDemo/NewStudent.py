import random


class Student:
    def __init__(self, no: int, height: float, weight: float):
        self.no = no
        self.height = height
        self.weight = weight

    def calculateBMI(self):
        BMI = self.weight / (self.height / 100) ** 2
        return round(BMI, 2)

    def toCsvLine(self):
        return (str(self.no) + ","
                + str(self.height) + ","
                + str(self.weight) + ","
                + str(self.calculateBMI()))

    @staticmethod
    def getCsvTitle():
        return "No,Height,Weight,BMI"  # 靜態方法(static method)


path = "./files"
# class裡的list
students = list()
# students.append("No, Height, Weight")
for n in range(1, 41):
    h = round(random.uniform(150, 180), 1)
    w = round(random.uniform(45, 70), 1)
    s = Student(n, h, w)
    # students.append(str(n) + "," + str(h) + "," + str(w))
    print(s.__dict__)
    students.append(s)
the_dir = path + "/students.csv"



# lines = list()
# lines.append(Student.getCsvTitle())
# for student in students:
#     lines.append(student.toCsvLine())

# with open(the_dir, "w") as f:
#     output = "\n".join(lines)
#     print(output)
#     f.write(output)
