import random
"""
# import random

array = ["A" , "B" , "C"]

print(array[0])

array.append("D")

array.insert(1,"B" )
print(array)

array.remove("B")
print(array)
print(array.count("D"))

array.reverse()
print(array)

# random.randint(a,b)=> 從a~b之間隨機取一個整數
num = random.randint(0,2)
print("random" + str(num))
"""

"""
# 剪刀石頭布

array = ["剪刀","石頭","布"]
me = int(input("input:"))
pc = random.randint(0, 2)
print(array[me])
print(array[pc])
if me == pc:
    print("平手")
else:
    if (me + 1) % 3 == pc:
        print("電腦贏")
    else:
        print("玩家贏")
"""

array=["棒", "老虎", "雞", "蟲"]
me = int(input("input:"))
pc = random.randint(0,3)
print(array[me])
print(array[pc])
if (me + 1) % 4 == pc:
    print("玩家贏")
elif (pc + 1) % 4 == me:
    print("電腦贏")
else:
    print("平手")

