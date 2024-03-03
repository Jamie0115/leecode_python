import random
"""
利用蒙地卡羅法來計算一個圓面積，
你可以想成有一個圓，先用一個正方形將它包起來，再隨機丟石頭在那個圓裡，
最後根據你丟進圓的數量除上總共丟出的石頭，就可以得到比例，而外面的面積乘上比例就可以得到圓的面積。
那因為樣本數越多就越準確，所以先設定總共執行n次
"""

n = int(input("n : "))

count = 0
incircle = 0
while count < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        incircle += 1
    else:
        pass
    count += 1

print("圓圈內:" + str(incircle))

ratio = incircle / n
print("正方形面積:", 4)
print("圓面積:", 4 * ratio)
