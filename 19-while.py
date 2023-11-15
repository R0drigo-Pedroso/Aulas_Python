gameName = input("Digite o nome do jogo\n")

qtdRating = 0
totalRating = 0
rating = 0
average = 0

while (rating != -1):
    rating = float(input("Informe a nota do jogo\n"))
    if (rating != -1):
        totalRating += rating  # totalRating = totalRating + rating
        qtdRating += 1  # qtdRating = qtdRating + 1
        average = totalRating / qtdRating
print(f"Média das Avaliações do jogo {gameName} é {average:.2f}")


""" 
Este código em Python solicita ao usuário o nome de um jogo e, em seguida, permite que o usuário insira várias avaliações para o jogo. O programa continua a solicitar avaliações até que o usuário insira -1. Em seguida, calcula e exibe a média das avaliações fornecidas.

1. **Entrada do Nome do Jogo:**
   - `gameName = input("Digite o nome do jogo\n")`: Solicita e armazena o nome do jogo fornecido pelo usuário.

2. **Avaliações e Cálculo da Média:**
   - `qtdRating`: Número total de avaliações.
   - `totalRating`: Soma total das avaliações.
   - `while True:`: Loop infinito.
   - `rating = float(input("Informe a nota do jogo (-1 para sair)\n"))`: Solicita e converte a avaliação do usuário para um número decimal.
   - `if rating == -1: break`: Se a avaliação for -1, encerra o loop.
   - `totalRating += rating`: Adiciona a avaliação à soma total.
   - `qtdRating += 1`: Incrementa o número total de avaliações.
   - `average = totalRating / qtdRating if qtdRating > 0 else 0`: Calcula a média, evitando a divisão por zero.

3. **Saída:**
   - `print(f"Média das Avaliações do jogo {gameName} é {average:.2f}")`: Exibe a média das avaliações do jogo com duas casas decimais.

Este código é um exemplo simples de entrada, processamento e saída, com a capacidade de lidar com múltiplas avaliações antes de finalizar o cálculo da média.
"""
