class Merchandise:
    __supplier = "Common Company"

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def getName(self) -> str:
        return self.__name

    def getPrice(self) -> float:
        return self.__price

    def do(self):
        self.__doA()
        self.__doB()
        self.__doC()

    def __doA(self):
        pass

    def __doB(self):
        pass

    def __doC(self):
        pass

    @classmethod
    def getSupplier(cls) -> str:
        return cls.__supplier

    @staticmethod
    def slogan() -> str:
        return "everybody come to buy, quickly"
