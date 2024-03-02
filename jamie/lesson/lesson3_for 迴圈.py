i = 0
while i < 5:
    print(i)
    i = i + 1

array = ["A", "B", "C", "D"]

for item in array:  # 這行為叫做traversal=>動詞
                    # iterable 可迭代的 =>形容詞
    print(item)

# range(start, stop, step)
# range(10) =>預設從0開始，到前一個數字
for index in range(len(array)):  # len(array)=>array的長度
    print(index)
    print(array[index])
