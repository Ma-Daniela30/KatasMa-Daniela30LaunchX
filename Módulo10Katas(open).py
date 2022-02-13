def main():
    try:
        open("marte.jpg")
    except OSError as err:
        if err.errno == 2:
            print("¡No se pudo encontrar el archivo marte.jpg!")
        elif err.errno == 13:
            print("Encontre marte.jpg pero no puedo leerlo")

        print("Tengo problema al intentar leer el archivo", err)


if __name__ == "__main__":
    main()
