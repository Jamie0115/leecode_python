import random

projects = ["chinese", "english", "math"]
path = "./files"

for i in range(17):
    for project in projects:
        lines = list()
        lines.append("No., Score")
        for no in range(1, 41):
            lines.append(str(no) + "," + str(random.randint(0,100)))
        the_dir = path + "/" + str(i) + "/" + project + ".csv"
        print(the_dir)
        with open(the_dir, "w") as f:
            output = "\n".join(lines)
            print(output)
            f.write(output)
