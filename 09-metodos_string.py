gameName = "Fifa 23"
gameDescription = """ Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports, e que possibilita jogar localmente ou online """


print(gameName.upper())  # Retornor string em maiúsculo
print(gameName.lower())  # Retornor string em manúsculo
print(gameName.capitalize())  # Apenas a primeira letra em maiúculo
print(gameName.title())  # Apenas a primeira letra em maiúsculo

# Retorna a string centralizada com caractere de preenchimento
print(gameName.center(10, '-'))
print(gameName.find("i"))  # Retorna a posição de um determinado caractere
print(gameDescription.count("f"))  # Conta caracteres
print(gameDescription.count("a"))  # Conta caracteres
print(gameDescription.replace("Fifa", "Pes"))  # Altera um elemento por outro
# Podemos acrescentar um elemento dentro do texto
print(gameDescription.split(','))
