import csv

def average(file_path, subject):
    total = 0
    count = 0
    with open(file_path, "r", encoding="utf-8-sig") as csvFile:
        reader = csv.DictReader(csvFile)  # 利用DictReader讀取 CSV 檔案
        for row in reader:
            if subject in row:  # 確保科目在標題中
                total += float(row[subject])
                count += 1
            else:
                print(f"Subject '{subject}' not found in the CSV file.")
                return None