array = ["A", "B", "C"]

array.append("D")
print(array)

array.insert(1,"D")
print(array)
print("count" + str(array.count("D")))

array.remove("D")
print(array)
print("count" + str(array.count("D")))

array.reverse()
print(array)
