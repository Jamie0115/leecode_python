from datetime import datetime
import random
# 獲取當前的日期和時間
now = datetime.now()

# 提取年月日時分秒
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
accountNumber = now.strftime("%Y%m%d-%H%M%S") + "-" + str(random.randint(1000,9999))
# 輸出結果
print(f"銀行帳戶: " + accountNumber)