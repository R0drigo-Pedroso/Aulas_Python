gameFifa = {
    "name": "Fifa 23",
    "yearLaunch": "2022",
    "gamePrice": "90.50",
    "classification": "8.9",
    "genre": ["esporte", "Familia"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))


# 1 - Recuperar um elemento do dicionario
print(gameFifa['genre'])
print(gameFifa.get('classification"'))

# 2 - Buscar apenas as chaves do dicionario
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionario
print(gameFifa.values())

# 4 - BUscar itens do dicionarios com chave e valores
print(gameFifa.items())

# 5 - Adicionar item no dicionario
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizar item no dicionario
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Remover item no dicionarios
gameFifa.pop("players")
print(gameFifa)
