"""
設計一個輸入密碼的程式，可以一直輸入直到對了為止
"""
password = "5566"

while True:
    string = input("Enter password : ")
    if string == password:
        print("Pass")
        break
    else:
        print("Error")

"""
設計一個輸入密碼的程式，可以一直輸入直到對了為止
也可以設定一個進階版的：當輸入幾次錯的之後便沒辦法再輸入了
"""
limit = 3
count = 0
while count < limit:
    count += 1
    string = input("Try Enter password , times " + str(count) + " : ")
    if string == password:
        print("Pass")
        break
    else:
        print("Error")
        continue

