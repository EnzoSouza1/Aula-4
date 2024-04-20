def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    comuns = set1.intersection(set2)

    apenas_na_lista1 = set1 - set2

    apenas_na_lista2 = set2 - set1

    elementos_unicos = set1.union(set2)

    lista_sem_repetidos_na_segunda = set1 - set2
    
    print("Valores comuns às duas listas:", comuns)
    print("Valores que só existem na primeira lista:", apenas_na_lista1)
    print("Valores que existem apenas na segunda lista:", apenas_na_lista2)
    print("Elementos não repetidos das duas listas:", elementos_unicos)
    print("Primeira lista sem os elementos repetidos na segunda:", lista_sem_repetidos_na_segunda)

def main():
    # Listas de exemplo
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    
    comparar_listas(lista1, lista2)

if __name__ == "__main__":
    main()
