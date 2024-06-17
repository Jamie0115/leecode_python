def wavelength():
    for pixel in range(1, 289):
        Wavelength = A0 + B1*pixel + B2*pixel**2 + B3*pixel**3 + B4*pixel**4 + B5*pixel**5
        print(Wavelength)
A0 = float(input("A0= "))
B1 = float(input("B1= "))
B2 = float(input("B2= "))
B3 = float(input("B3= "))
B4 = float(input("B4= "))
B5 = float(input("B5= "))
print(wavelength())