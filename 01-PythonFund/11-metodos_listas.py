gameList = [
    'Resident Evil',
    'Star Wars Jeri Survivor',
    'The Legend fo Zelda',
    'Red Dead 2',
    'Mario Odyssey',
    'Luigis Mansion 3'
]

# 1 - Tamanho da Lista
print(len(gameList))

# 2 - Recuperar um item da lista pelo indice
print(gameList.index('Mario Odyssey'))

# 3 - Adicionar item ao final da lista
gameList.append("Gta V")
print(gameList)

# 4 - Ordem a lista
gameList.sort()
print(gameList)

# 5 - Copiar os item de um lista para outra
gameReset = gameList.copy()
gameReset.remove('Mario Odyssey')
print(gameReset)

# 6 - Remove todos os item da lista
gameList.clear()
print(gameList)
