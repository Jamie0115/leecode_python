# 1. primeNumList [] => 放質數的list
# 2. range 2~n，每個數字除以primeNumList的每個質數，如果都不能整除，這個數字就是質數

def all_pass(current_list, current_num):
    for index in current_list:
        if current_num % index == 0:
            return False
        else:
            pass
    return True


num = int(input("Input number : "))

primeNumList = list()
for i in range(2, num + 1):
    if all_pass(primeNumList, i):
        primeNumList.append(i)

print(primeNumList)
