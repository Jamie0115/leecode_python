import random
""""
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
"""

# random.randint(a,b) => 從a~b之間隨機取一個整數
"""
array = ["剪刀", "石頭", "布"]
me = int(input("[0]剪刀 [1]石頭 [2]布 : "))
pc = random.randint(0, 2) # 0,1,2

print("玩家：" + array[me])
print("電腦：" + array[pc])

if me == pc:
    print("平手")
else:
    if (me+1)%3 == pc:
        print("電腦贏")
    else:
        print("玩家贏")
"""

array = ["棒", "老虎", "雞", "蟲"]
me = int(input("[0]棒 [1]老虎 [2]雞 [3]蟲: "))
pc = random.randint(0, 3) # 0,1,2,3

print("玩家：" + array[me])
print("電腦：" + array[pc])

if me == (pc+1)%4:
    print("電腦贏")
elif pc == (me+1)%4:
    print("玩家贏")
else:
    print("平手")
