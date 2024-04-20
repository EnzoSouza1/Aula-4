def contar_caracteres(frase):
    contagem = {}
    
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    
    return contagem

def main():
    frase = input("Digite uma frase: ")
    
    resultado = contar_caracteres(frase)
    
    print(resultado)

if __name__ == "__main__":
    main()
