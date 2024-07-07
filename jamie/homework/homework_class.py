
# 銀行帳戶
# 設計一個銀行帳戶類別（Account），每個帳戶都有自己的帳號（account_number）、所有者的姓名（owner_name）、餘額（balance），並提供以下功能：

# 存款（deposit）
# 提款（withdraw）
# 查詢帳戶信息（get_account_info）
# 轉賬（transfer），將款項從一個帳戶轉移到另一個帳戶

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self, amount):
        return self.balance + amount
    def withdraw(self, amount):
        return self.balance - amount
    @staticmethod
    def get_account_info():
        return {
            "Account Number : self.account_number,"
            "Owner Name : {self.owner_name}",
            "Balance : {self.balance}"
        }
    def transfer(self, target_account, amount):
        if amount > self.balance:
            return {"Insufficient funds"}
        self.balance -= amount
        target_account.balance += amount