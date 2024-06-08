import csv
test1_path = "C:/Users/funny/Desktop/count/test1.csv"
test2_path = "C:/Users/funny/Desktop/count/test2.csv"
count_path = "C:/Users/funny/Desktop/count"
# 讀取 test1.csv
resultMap1 = dict()
with open(test1_path, mode='r', newline='') as test1:
    # reader1 = csv.reader(test1)
    reader1 = csv.DictReader(test1)
    for row in reader1:
        pixel1 = row.get('pixel') # 第一筆資料
        value1 = row.get('intensity')  # 取得第一筆資料的 Value 欄位值
        resultMap1[int(pixel1)] = int(value1)

# 讀取 test2.csv
with open(test2_path, mode='r', newline='') as test2:
    reader2 = csv.reader(test2)
    next(reader2)  # 跳過標題行
    next(reader2)  # 跳過第一筆資料
    row2 = next(reader2)  # 第二筆資料
    value2 = int(row2[1])  # 取得第二筆資料的 Value 欄位值
    print(value2)
# 計算差值
value_diff = value1 - value2
# 寫入結果到新的 CSV 檔案
with open(count_path, mode='w', newline='') as result_file:
    writer = csv.writer(result_file)
    # 寫入標題行
    writer.writerow(['ID', 'Value_diff'])
    # 寫入計算結果
    writer.writerow([row1[0], value_diff])
    print(f'Result saved to {result_file}')