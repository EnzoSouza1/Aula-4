pessoa1 = {
    "primeiro_nome": "Enzo",
    "sobrenome": "Rodrigo",
    "idade": 20,
    "cidade": "Brasilia"
}

pessoa2 = {
    "primeiro_nome": "Maria",
    "sobrenome": "Santos",
    "idade": 25,
    "cidade": "Rio de Janeiro"
}

pessoa3 = {
    "primeiro_nome": "Carlos",
    "sobrenome": "Oliveira",
    "idade": 35,
    "cidade": "Belo Horizonte"
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("\nInformações sobre a pessoa:")
    print("Primeiro nome:", pessoa["primeiro_nome"])
    print("Sobrenome:", pessoa["sobrenome"])
    print("Idade:", pessoa["idade"])
    print("Cidade:", pessoa["cidade"])
