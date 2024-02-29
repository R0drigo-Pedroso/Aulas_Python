""" 
Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:

1. Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
2. Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
3. Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.

"""
import random

def gerarNumeroAleatorio(comeco, fim):
    return random.randint(comeco, fim)


intervaloInicial = 0
intervaloFinal = 10

while True:
    numeroSorteado = gerarNumeroAleatorio(intervaloInicial, intervaloFinal)
    
    numeroUsuario = input("Escolha um número entre 0 a 10: ")
    
    if numeroUsuario.lower() == 'sair':
        print("Programa encerrado")
        break
    
    try:
        numeroUsuario = int(numeroUsuario)
    except ValueError:
        print("Por favor, digite um número válido")
        continue
    
    if numeroUsuario < intervaloInicial or numeroUsuario > intervaloFinal:
        print("Por favor, digite um número dentro do intervalo especificado")
    elif numeroUsuario == numeroSorteado:
        print("Parabéns! você acertou o número sorteado", numeroSorteado)
    else:
        print("Você errou. O número sorteado foi", numeroSorteado)