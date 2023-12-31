import random

# Números mais sorteados desde 2009
mais_sorteados = [3, 5, 10, 20, 33, 36]

# Números que nunca saíram desde 2009
nunca_sairam = [7, 8, 9, 13, 19, 21, 26, 28, 39, 44, 48, 54, 59, 60]

# Função para gerar uma dica sem números repetidos


def gerar_dica(sem_repeticao=True):
    if sem_repeticao:
        dica = random.sample(range(1, 61), 6)
    else:
        dica = random.choices(range(1, 61), k=6)
    return dica


# Dica 1: Combinação com números mais sorteados e alguns que nunca saíram
dica1 = mais_sorteados + random.sample(nunca_sairam, 2)

# Dica 2: Combinação com mais números que nunca saíram
dica2 = random.sample(nunca_sairam, 6)

# Dica 3: Combinação balanceada entre mais sorteados e alguns que nunca saíram
dica3 = random.sample(mais_sorteados, 3) + random.sample(nunca_sairam, 3)

# Dica 4: Combinação com repetição de números mais sorteados
dica4 = gerar_dica(sem_repeticao=False)

# Dica 5: Combinação com alguns dos mais sorteados e alguns que nunca saíram
dica5 = random.sample(mais_sorteados, 4) + random.sample(nunca_sairam, 2)

# Imprimir as dicas
print("Dica 1:", dica1)
print("Dica 2:", dica2)
print("Dica 3:", dica3)
print("Dica 4:", dica4)
print("Dica 5:", dica5)
