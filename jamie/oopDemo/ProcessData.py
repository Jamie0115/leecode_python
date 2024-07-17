from BusinessObject import BankAccount
import random

PATH = "./data"


def createAccount(accountName: str) -> BankAccount:
    print("建立一個BankAccount")
    bankAccount = BankAccount("", accountName, 1000)
    return bankAccount


def save(data: BankAccount):
    print("存一個BankAccount進csv")


def readByAccountNumber(accountNumber: int) -> BankAccount:
    pass


name = input("Input Account Name:")
save(createAccount(name))
