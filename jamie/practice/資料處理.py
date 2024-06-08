import csv
test1_path = "C:/Users/funny/Desktop/test1.csv"
test2_path = "C:/Users/funny/Desktop/test2.csv"
# 讀取 file1.csv
with open(test1_path, mode='r', newline='') as test1:
    reader1 = csv.reader(test1_path)
    next(reader1)  # 跳過標題行
    row1 = next(reader1)  # 第一筆資料
    value1 = int(row1[1])  # 取得第一筆資料的 Value 欄位值