from BusinessObject import BankAccount
from datetime import datetime
import random
import csv

PATH = "./data"
ACCOUNT_FILE = "/account.csv"
LEDGER_FILE = "/ledger.csv"

# 創建帳戶資料
def createAccount(accountName: str) -> BankAccount:
    # 獲取當前時間，用於生成唯一的帳戶號碼
    now = datetime.now()
    accountNumber = now.strftime("%Y%m%d-%H%M%S") + "-" + str(random.randint(1000, 9999))
    # 創建 BankAccount 物件
    bankAccount = BankAccount(accountNumber, accountName, 1000)
    print("建立一個BankAccount : " + bankAccount.accountInfo())
    return bankAccount

# 存一個新的帳戶進去csv檔
def saveNewAccount(data: BankAccount):
    print("存一個BankAccount進csv")
    with open(PATH + ACCOUNT_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + data.accountCsvLine())
    saveNewTransactionRecord(data.getAccountNumber(), data.getBalance())

# 顯示交易紀錄
def saveNewTransactionRecord(number: str, amount: int):
    with open(PATH + LEDGER_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + number + "," + str(amount))

# 讀取整筆csv檔的資料
def readByAccountNumber(accountNumber: str) -> BankAccount:
    with open(PATH + ACCOUNT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            number = row["AccountNumber"]
            name = row["AccountName"]
            if number == accountNumber:
                balance = getBalanceByAccountNumber(number)
                return BankAccount(number, name, balance)


def getBalanceByAccountNumber(accountNumber: str) -> int:
    balance = 0
    with open(PATH + LEDGER_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["AccountNumber"] == accountNumber:
                balance += int(row["Amount"])
    return balance

