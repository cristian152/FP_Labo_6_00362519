def fahrenheit_celsius():
    '''convierte temperatura en grados fahrenheit a grados celsius'''

    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    return "{} grados Fahrenheit son {} grados Celsius".format(fahrenheit, celsius)

def celsius_fahrenheit():
    '''convierte temperatura en grados celsius a fahrenheit'''

    celsius = int(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = 9.0/5.0 * celsius +32
    return "{} grados Celsius son {} grados Fahrenheit".format(fahrenheit, celsius)

def kelvin_celsius():
    '''convertidor de kelvin a celsius'''
    kelvin = int(input("ingrese la temperatura en kelvin: "))
    celsius = (kelvin-273.2)
    return "{} grados kelvin son {} grados celsius". format(kelvin, celsius)
while True:
    print("1.- Fahrenheit a Celsius")
    print("2.- Celsius a Fahrenheit")
    print("3.- kelvin a celsius")
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion == 3:
            print (kelvin_celsius())
        else:
            raise ValueError
    except ValueError:
        print("Ingrese solo números.(1/2/3)")