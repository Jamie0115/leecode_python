#  1. 先寫function，構思整個題目的邏輯

def Zerocount(n):  # 先有function的架構
    count = 0  # 一開始0出現的次數(初設為0)
    max_count = 0  # 讓max_count隨時記錄最大值
    while n > 0:  # 假設我的數字n大於零
        d = n % 10  # 取得其個位數字
        if d == 0:  # 若個位數字為0
            count += 1  # 計數器count+1
            max_count = max(max_count, count)  # 紀錄最多max_count的次數
        else:
            count = 0  # 如果個位數字不為0，計數器歸零
        n = n // 10  # 這時候的經while計算的n在重新去除個位數字->得到新數n
    return max_count

#  2. 在輸入n值，print出max_count
n = int(input("Number: "))
print(Zerocount(n))

"""
n = int(input("Number: "))
count = 0  # 一開始0出現的次數(初設為0)
max_count = 0  # 讓max_count隨時記錄最大值
while n > 0:  # 假設我的數字n大於零
    d = n % 10  # 取得其個位數字
    if d == 0:  # 若個位數字為0
        count += 1  # 計數器count+1
        max_count = max(max_count, count)
    else:
        count = 0  # 如果個位數字不為0，計數器歸零
    n = n // 10  # 這時候的經while計算的n在重新去除個位數字->得到新數n
print(max_count)
"""


