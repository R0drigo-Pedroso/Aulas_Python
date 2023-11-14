""" 
## Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.


## Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.

"""

# Calculo da distância.
dist = float(input("Digite o valor da distância\n"))

if dist <= 200:
    resp = dist * 0.50
elif dist > 201:
    resp = dist * 0.35
else:
    print("Erro no calculo")
    resp = 0

print(f"Resultado é: R$ {resp:.2f}")


# Calcule Aumento de Salario.
salarioAtual = float(input("Digite seu salario Atual\n"))
perc_increase = 0.15

if salarioAtual > 1250:
    perc_increase = 0.10
increase = salarioAtual * perc_increase

print(f"Resultado é: R$ {increase:.2f}")
