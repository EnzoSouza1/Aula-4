pet1 = {
    "nome": "Rex",
    "tipo": "Cachorro",
    "dono": "Enzo"
}

pet2 = {
    "nome": "Pandora",
    "tipo": "Gato",
    "dono": "Maria"
}

pet3 = {
    "nome": "Nemo",
    "tipo": "Peixe",
    "dono": "Carlos"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nInformações sobre o animal de estimação:")
    print("Nome:", pet["nome"])
    print("Tipo:", pet["tipo"])
    print("Dono:", pet["dono"])
