class Wavelength():
    def __init__(self, a0: float, b1: float, b2: float, b3: float, b4: float, b5: float):
        self.__a0 = a0
        self.__b1 = b1
        self.__b2 = b2
        self.__b3 = b3
        self.__b4 = b4
        self.__b5 = b5

    def getIntensity(self, pixel: int):
        return self.__calculate(pixel)

    def __calculate(self, pixel: int):
        return (self.__a0
                + self.__b1 * pixel
                + self.__b2 * pixel**2
                + self.__b3 * pixel**3
                + self.__b4 * pixel**4
                + self.__b5 * pixel**5)


def run():
    a = Wavelength(100.2, 200.5, 234, 100.4, 66.6, 99.8)
    for i in range(1, 11):
        print(a.getIntensity(i))


run()


