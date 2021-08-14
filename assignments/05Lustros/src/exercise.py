def main():
    #escribe tu código abajo de esta línea
    nacer = float(input("Dame el año de nacimiento: "))
    año = float(input("Dame el año actual: "))
    edad = año - nacer
    lustros = edad/5
    print("Los lustros que has vivido son:",lustros)


if __name__ == '__main__':
    main()
