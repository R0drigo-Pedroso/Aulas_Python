name = input("Digite o nome do Jogo\n")
yearLaunch = int(input("Digite o Ano de Lançamento do Jogo\n"))
gamePrice = float(input("Digite o preço do Jogo\n"))
planIcluded = input("Está incluso no serviço mensal?\n")

print("###Dados do Jogo###")
print("===================")

""" Forma alternativa 1 """
""" print("Nome do Jogo:", name)
print("Ano do Jogo:", yearLaunch)
print("Preço do Jogo:", gamePrice)
print("Está incluído no plano?", planIcluded)
 """

# Alternativa 2
""" print("nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
      "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIcluded) """

# Alternativa 3
print(f"Nome do Jogo: {name} \n Ano do Lançamento: {yearLaunch} \n Preço do Jogo: {gamePrice} \n Está incluso no serviço?: {planIcluded}")
