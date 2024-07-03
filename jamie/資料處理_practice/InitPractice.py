import random
class Student:
    def __init__(self, No:int, Height:float, Weight:float):
        self.No = No
        self.Height = Height
        self.Weight = Weight
    def BMI(self):
        bmi = self.Weight / (self.Height / 100)**2
        print(bmi)

path = "./files2"

students = list()
students.append("No, Height, Weight")
for no in range(1, 41):
    height = random.randint(150, 180)
    weight = random.randint(45, 70)
    students.append(str(no) + "," + str(height) + "," + str(weight))
the_dir = path + "/students.csv"
print(the_dir)
print(students)

with open(the_dir, "w") as f:
    output = "\n".join(lines)
    print(output)
    f.write(output)