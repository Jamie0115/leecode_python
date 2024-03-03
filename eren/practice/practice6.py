import random
"""
終極密碼
主持人會讓你在1~100猜一個數字，
假設正確數字是50，如果你猜70，主持人會改讓你在1~70猜一個，
如果你猜20，主持人會再讓你在30~70猜一個，
簡單來說就是主持人會幫你不斷縮小範圍直到被猜對為止
"""

target = random.randint(1, 100)

top = 100
bottom = 1
while True:
    num = int(input(f"Input number ({bottom} ~ {top}) : "))
    if num == target:
        print("Congratulations!")
        break
    elif num > target:
        print("too large")
        top = num
    elif num < target:
        print("too less")
        bottom = num
    else:
        pass
