"""
a. int() 轉成整數
b. float() 轉成小數
c. str() 轉成字串
"""
"""
BMI = 體重(公斤) / 身高2(公尺2)
體重過輕:BMI ＜ 18.5
正常範圍:18.5≦BMI＜24
異常範圍:過重：24≦BMI＜27
輕度肥胖：27≦BMI＜30
中度肥胖：30≦BMI＜35
重度肥胖：BMI≧35
"""
## x=體重
## y=身高
str_x = input("x: ")
str_y = input("y:")
num_x = float(str_x)
num_y = float(str_y)

z = num_x / (num_y*num_y)

print(z)
if(z < 18.5):
    print("thin")
elif( z >= 18.5 and z < 24):
    print("moderate")
elif (z >= 24 and z < 27):
    print("fat")
elif (z >= 27 and z < 30):
    print("light fat")
elif (z >= 30 and z < 35):
    print("moderate fat")
else:
    print("too fat")
