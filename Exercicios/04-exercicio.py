""" 
## Contagem Regressiva
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
"""

""" import winsound
x = 10
while x >= 0:
    print(x)
    x -= 1
winsound.Beep(2500, 300)
 """

"""
## Tabuada
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
"""

number = int(input("Qual Tabuada você quer calcular: \n"))
end = int(input("Até qual número que calcular: \n"))
# begin = int(input("De: \n"))

x = 1

while x <= end:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x = x + 1
