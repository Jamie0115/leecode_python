# 銀行帳戶
# 設計一個銀行帳戶類別（Account），每個帳戶都有自己的帳號（account_number）、所有者的姓名（owner_name）、餘額（balance），並提供以下功能：

# 存款（deposit）
# 提款（withdraw）
# 查詢帳戶信息（get_account_info）
# 轉賬（transfer），將款項從一個帳戶轉移到另一個帳戶

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
                .format(accountNumber = self.__accountNumber, accountName = self.__accountName, balance = self.__balance))

    # 轉賬（transfer），將款項從一個帳戶轉移到另一個帳戶
    def transfer(self, target_account: str, amount: int) -> str:
        if target_account == self.__accountNumber:
            return "目標帳戶不可與來源帳戶相同"

        if self.__balance < amount:
            return "金額不足"

        self.__balance -= amount
        return ("轉帳帳戶: {target_account}, 轉帳金額: {amount}, 帳戶餘額: {balance}"
                .format(target_account = target_account, amount = amount, balance = self.__balance))


bank = BankAccount("123456789000000", "Jamie", 1000)
while True:
    mode = input("檢查餘額:0 存款:1 提款:2 帳戶訊息:3 轉帳:4 離開:5\n"
                 "請輸入:\n")

    match mode:
        case "0":
            print("目前存款餘額:" + str(bank.balance()))
        case "1":
            deposit_amount = int(input("請輸入存入的金額:"))
            print("存入後的存款金額:", bank.deposit(deposit_amount))
        case "2":
            withdraw_amount = int(input("請輸入欲提款的金額:"))
            print("提款後的餘額:", bank.withdraw(withdraw_amount))
        case "3":
            print("帳戶信息:", bank.accountInfo())
        case "4":
            target_account_number = input("轉帳帳戶號碼: ")
            target_account_amount = int(input("轉帳金額: "))
            print(bank.transfer(target_account_number, target_account_amount))
        case "5":
            print("謝謝,請取卡~")
            break
        case _:
            print("執行錯誤，請輸入正確數字")

    # if mode == 0:
    #     print("目前存款餘額:" + str(bank.balance()))
    # elif mode == 1:
    #     deposit_amount = int(input("請輸入存入的金額:"))
    #     print("存入後的存款金額:", bank.deposit(deposit_amount))
    # elif mode == 2:
    #     withdraw_amount = int(input("請輸入欲提款的金額:"))
    #     print("提款後的餘額:", bank.withdraw(withdraw_amount))
    # elif mode == 3:
    #     print("帳戶信息:", bank.accountInfo())
    # elif mode == 4:
    #     target_account_number = input("轉帳帳戶號碼: ")
    #     target_account_amount = int(input("轉帳金額: "))
    #     print(bank.transfer(target_account_number, target_account_amount))
    # elif mode == 5:
    #     print("謝謝,請取卡~")
    #     break
    # else:
    #     print("執行錯誤，請輸入正確數字")
