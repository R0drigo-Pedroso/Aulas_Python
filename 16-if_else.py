name = input("Digite o nome do jogo\n")
yearLauch = int(input("Digite o ano de lançamento do jogo\n"))
classification = float(input("Digite a nota de classificação do jogo\n"))

if classification > 8.0 and yearLauch > 2015:
    print(f"O jogo {name} é bom. Recomento jogá-lo")
else:
    print(f"Jogo {name} ainda não atigiu uma boa nota. Por isso não recomendo")


""" 
Explicação do código acima:

Este código em Python solicita informações ao usuário sobre um jogo, incluindo nome, ano de lançamento e nota de classificação. Em seguida, verifica se o jogo possui uma classificação superior a 8.0 e foi lançado após 2015. Se ambas as condições forem verdadeiras, imprime uma recomendação positiva para jogar o jogo. Caso contrário, indica que o jogo não atingiu uma boa nota e, portanto, não é recomendado.

Além disso, é possível utilizar outros operadores lógicos, como "and" e "or", para modificar as condições no mesmo código.
"""

""" 
Nessa aula, destacou-se a importância da endentação no código Python para melhorar a legibilidade. Notavelmente, é crucial notar que, ao contrário de outras linguagens, o Python não requer o uso de chaves ou colchetes para estruturar o código, tornando-o mais conciso e limpo.
"""
