gamesSet = {
    "Fifa23",
    "Red Dead 2",
    "Strar Wars",
    "Mario Odyssesy",
    "The Legend of Zelda"
}

print(gamesSet)

# Não possibilita recuperar valores via fatiamento ou slice

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {
    "Fifa23",
    True,
    1,
    90.50
}

print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item do set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)


""" 
Set me possibilita a usar outras tecnicas para manipulação de Dados buscando, mas não é possivel realizar o fatiamento entre as informações.
"""
