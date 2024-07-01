import random

path = "./files2"

lines = list()
lines.append("No., Height, Weight")
for no in range(1, 41):
    height = random.randint(150, 180)
    weight = random.randint(45, 70)
    lines.append(str(no) + "," + str(height) + "," + str(weight))
the_dir = path + "/students.csv"
print(the_dir)
print(lines)

with open(the_dir, "w") as f:
    output = "\n".join(lines)
    print(output)
    f.write(output)
