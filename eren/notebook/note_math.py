import math
# ----------------------------------------------------------------

# math.pi : π
print("math.pi:", math.pi)

# math.e : 數學常數
print("math.e:", math.e)

# math.inf : 無窮大
print("math.inf:", math.inf)

# math.nan : 不是一個數，如 0 * ∞(無限大)
print("math.nan:", math.nan)

# math.fabs(a) : 取絕對值(返回浮點數)
print("math.fabs(-10):", math.fabs(-10))

# math.factorial(a) : a階乘，= a!
print("math.factorial(5):", math.factorial(5))

# math.ceil(a) : 天花板函數，傳回大於等於a的最小整數
print("math.ceil(5.5):", math.ceil(5.5))

# math.floor(a) : 地板函數，傳回小於等於a的最大整數
print("math.floor(5.5):", math.floor(5.5))

# math.gcd(a,b) : 計算a和b的最大公因數
print("math.gcd:", math.gcd(105, 252))

# math.isnan(a) : 判別a是否為有界的數(不是正負無限大)
print("math.isfinite(100):", math.isfinite(100))

# math.isnan(a) : 判別a是否為正無限大或負無限大
print("math.isinf(math.inf):", math.isinf(math.inf))

# math.isnan(a) : 判別a是否為nan
print("math.isnan(0 * math.inf):", math.isnan(0 * math.inf))

# ----------------------------------------------------------------

# math.exp(a) : 計算e^a，其中e=數學常數2.718281828
print("math.exp(10):", math.exp(10))

# math.log(a,base) : log(a,base)是以base為底的對數，log(a)是以e為底
print("math.log(1024, 2):", math.log(1024, 2))

# math.pow(a,b) : a^b，返回浮點數
print("math.pow(2, 10):", math.pow(2, 10))

# math.sqrt(a) : 將a開根號
print("math.sqrt(100):", math.sqrt(100))

# math.radians(a) : 將角度a轉換成弧度(radian)
print("math.math.radians(60):", math.radians(30))

# math.degrees(a) : 將弧度a轉換成角度(degree)
print("math.degrees():", math.degrees(math.pi / 4))

# math.sin(a) : 正弦函數，a的單位是弧度｜cos(a)是餘弦函數｜tan(a)是正切
print("math.sin(10):", math.sin(math.radians(30)))

# ----------------------------------------------------------------
