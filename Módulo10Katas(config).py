def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("No se puede encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Encontré config.txt pero es un directorio, no pude leerlo")
    except (BlockingIOError, TimeoutError):
        print(
            "Sistema de archivos con mucha carga, no se puede completar la lectura del archivo de configuración"
        )


if __name__ == "__main__":
    main()
