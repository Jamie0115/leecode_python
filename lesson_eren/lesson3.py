i = 0
while i < 5:
    # print(i)
    i = i + 1

array = ["A", "B", "C", "D"]
# traversal => 動詞
# iterable => 形容詞
# for item in array:
    # print(item)

# range(start, stop, step)
# range(10)  # 預設從0開始，產生到10的前面一個數字 => 0~9
for index in range(len(array)):
    print(index)
    print(array[index])
