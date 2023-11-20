# 1 - Função para imprimir Hello World
def wellcome():
    print("Hello Word")


wellcome()


# 2 - Função para somar dois numeros
def sum():
    # print(5 + 4)
    return 5 + 4


print(sum())

# 3 - Função para cadastrar um jogo


def create_game():
    name = input("Digite o nome do Jogo\n")
    yearLaunch = int(input("Digite o Ano de Lançamento do Jogo\n"))
    gamePrice = float(input("Digite o preço do Jogo\n"))
    planIcluded = float(input("Digite a nota de avaliação do Jogo\n"))

    print(f"{name} - R$ {gamePrice}")


create_game()
create_game()
