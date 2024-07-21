class BankAccount:
    def __init__(self, accountNumber: str, accountName: str, balance: int):
        self.__accountNumber = accountNumber
        self.__accountName = accountName
        self.__balance = balance

    # 存款（deposit）
    def deposit(self, amount):
        self.__balance += + amount
        return self.__balance

    # 提款（withdraw）
    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    # 餘額查詢(balance)
    def balance(self):  # READ
        return self.__balance

    def accountInfo(self):
        return ("帳戶號碼: {accountNumber}, 帳戶名字: {accountName}, 帳戶餘額: {balance}"
                .format(accountNumber=self.__accountNumber, accountName=self.__accountName, balance=self.__balance))

    # 轉賬（transfer），將款項從一個帳戶轉移到另一個帳戶
    def transfer(self, target_account: str, amount: int) -> str:
        if target_account == self.__accountNumber:
            return "目標帳戶不可與來源帳戶相同"

        if self.__balance < amount:
            return "金額不足"

        self.__balance -= amount
        return ("轉帳帳戶: {target_account}, 轉帳金額: {amount}, 帳戶餘額: {balance}"
                .format(target_account=target_account, amount=amount, balance=self.__balance))

    def accountCsvLine(self):
        return ",".join([str(self.__accountNumber), str(self.__accountName)])

    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self.__balance
