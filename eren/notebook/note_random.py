import random

# ----------------------------------------------------------------

# random.seed(s) : 設定亂數的種子為s
# random.seed(1000)

# random.random() : 產生0~1之間的亂數
print("random.random():", random.random())

# random.randint(a, b) : 產生介於a~b之間的整數亂數(包含a,b)
print("random.randint(0, 100):", random.randint(0, 100))

# random.uniform(a, b) : 產生介於a~b之間的浮點數亂數
print("random.uniform(0, 100):", random.uniform(0, 100))

# random.randrange(a,b,s) : 從a~b(不含)，間隔s隨機產生一個整數
print("random.randrange(0, 100, 3):", random.randrange(0, 100, 3))

# random.choice(obj) : 從obj中隨機選取一個元素，obj可以是字串或其他有序的資料型別
print("random.choice(['a', 'b', 'c', 'd', 'e']):", random.choice(['a', 'b', 'c', 'd', 'e']))

# random.sample(obj, k) : 從obj中隨機取得k個元素
print("random.sample(['a', 'b', 'c', 'd', 'e'], 2):", random.sample(['a', 'b', 'c', 'd', 'e'], 2))

# random.shuffle(lst) : 將list中的元素打亂(不是直接return)
lst = ['a', 'b', 'c', 'd', 'e']
random.shuffle(lst)
print("random.shuffle(lst):", lst)

# ----------------------------------------------------------------
