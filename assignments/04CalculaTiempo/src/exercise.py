def main():
    #escribe tu código abajo de esta línea
    age = int(input("Dame tu edad: "))
    year = int(input("Dame el año actual: "))
    nacimiento = year-age
    futuro = nacimiento + 100
    print("Cumplirás 100 años en el año:",futuro)

if __name__ == '__main__':
    main()
