import pprint

gamesDict = {
    "resident evil 4": {
        "yearLaunch": "2023",
        "classification": "9.5",
        "genre": ["ação", "aventura"]
    },
    "Mario odyssey": {
        "yearLaunch": "2017",
        "classification": "9.8",
        "genre": ["aventura", "3d"]
    },
    "Fifa 23": {
        "yearLaunch": "2022",
        "classification": "8.9",
        "genre": ["esporte", "Familia"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)


# 1 - Buscar informação dentro de um dicionario aninhado
print(gamesDict["Mario odyssey"]["genre"])

# 2 - Adicionar novo item
gamesDict["Mario odyssey"]["Players"] = 1
print(gamesDict["Mario odyssey"])


# 3 - Excluir um dicionario
del gamesDict["resident evil 4"]
pp.pprint(gamesDict)
