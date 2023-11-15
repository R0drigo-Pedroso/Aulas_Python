# 1 - Lista valores de 0 a 10 que sejam menor do que 4
""" for i in range(10):
    if i < 4:
        print(i)
 """
listNumber = [i for i in range(10) if i < 4]
print(listNumber)

gamesList = [
    'Resident Evil',
    'Star Wars Jeri Survivor',
    'The Legend fo Zelda',
    'Red Dead 2',
    'Mario Odyssey',
    'Luigis Mansion 3'
]

# 2 - Jogos que possuam a letra v
newList = [x for x in gamesList if "v" in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gamesList if x != "Mario Odyssey"]
print(gamesFinished)

""" 
O que List Comprehension: 
List Comprehension é uma construção sintática em linguagens de programação que oferece uma forma concisa e expressiva de criar listas. Essa expressão é especialmente útil quando se deseja gerar, transformar ou filtrar elementos de uma lista, iterando sobre uma sequência de dados. A estrutura básica da List Comprehension inclui uma expressão principal, uma variável de iteração e, opcionalmente, uma condição de filtragem. Essa construção é considerada uma abstração de alto nível, proporcionando uma alternativa mais compacta e legível em comparação com a abordagem tradicional de usar loops `for` para construir listas.

Certamente, vou fornecer uma explicação mais concisa e acadêmica para o seu código:

1. **List Comprehension com Condição:**
   - `listNumber = [i for i in range(10) if i < 4]`: Cria uma lista contendo números de 0 a 3 usando list comprehension com uma condição de filtragem (`if i < 4`).

2. **Filtragem de Jogos por Letra:**
   - `newList = [x for x in gamesList if "v" in x]`: Cria uma nova lista contendo jogos que possuem a letra 'v' usando list comprehension.

3. **Filtragem de Jogos Concluídos:**
   - `gamesFinished = [x for x in gamesList if x != "Mario Odyssey"]`: Cria uma lista de jogos concluídos, excluindo "Mario Odyssey" usando list comprehension.

Em resumo, esses trechos de código demonstram o uso de list comprehension para criar listas de forma concisa e eficiente, filtrando elementos com base em condições específicas.
"""
