def comparar_versoes(versao_inicial, versao_alterada):
    set_versao_inicial = set(versao_inicial)
    set_versao_alterada = set(versao_alterada)

    elementos_nao_modificados = set_versao_inicial.intersection(set_versao_alterada)
    
    novos_elementos = set_versao_alterada - set_versao_inicial

    elementos_removidos = set_versao_inicial - set_versao_alterada

    print("Elementos que não mudaram:", elementos_nao_modificados)
    print("Novos elementos adicionados:", novos_elementos)
    print("Elementos removidos:", elementos_removidos)

def main():
    # Listas de exemplo
    versao_inicial = [1, 2, 3, 4, 5]
    versao_alterada = [3, 4, 6, 7, 8]

    comparar_versoes(versao_inicial, versao_alterada)

if __name__ == "__main__":
    main()
