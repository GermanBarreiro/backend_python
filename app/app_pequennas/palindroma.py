def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    
    return palabra == palabra[::-1]

def main():
    palabra = input("Introduce una palabra o frase: ")
    
    if es_palindromo(palabra):
        print(f"'{palabra}' es un paliindromo.")
    else:
        print(f"'{palabra}' no es un paliindromo.")

if __name__ == "__main__":
    main()