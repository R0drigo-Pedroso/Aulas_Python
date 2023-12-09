gamesTuple = ("Fifa23", "Red Dead 2", "Strar Wars",
              "Mario Odyssesy", "The Legend of Zelda")


print(gamesTuple)
print(type(gamesTuple))

# name = ("Rodrigo")
# print(type(name))

# - não possibilidade adicionar valores na tupla
# - não possibilidade remover valores na tupla
# - não possibilidade ordenar valores na tupla

# 1 - BUscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o último item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recupera um item da tupla pelo indice
print(gamesTuple.index("Red Dead 2"))

""" 
Tupla é uma forma de trabalhar com fatiamento, quando não temos itens para adicionar ou remover do texto ou lista que está sendo trabalhada.
Porém o fatiamento em python é muito importante pois facilita trabalhar com manutenção de dados e manipulação de informações

"""
