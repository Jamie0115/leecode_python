"""
a. int() 轉成整數
b. float() 轉成小數
c. str() 轉成字串
"""
"""
BMI = 體重(公斤) / 身高^2(公尺^2)
體重過輕 : BMI < 18.5
正常範圍 : 18.5 <= BMI < 24
體重過重： 24 <= BMI < 27
輕度肥胖： 27 <= BMI < 30
中度肥胖： 30 <= BMI < 35
重度肥胖： 35 <= BMI
"""
height = float(input("身高(公斤):"))
weight = float(input("體重(公斤):"))

BMI = weight / (height**2)

print("BMI:" + str(BMI))

if BMI < 18.5:
    print("體重過輕")
elif BMI >= 18.5 and BMI < 24:
    print("正常範圍")
elif BMI >= 24 and BMI < 27:
    print("體重過重")
elif BMI >= 27 and BMI < 30:
    print("輕度肥胖")
elif BMI >= 30 and BMI < 35:
    print("中度肥胖")
else:
    print("重度肥胖")
