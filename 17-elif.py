num1 = float(input("Digite o primeiro número\n"))
num2 = float(input("Digite o segundo número\n"))

operation = input("Digite a operação a realizar (+ - * / )\n")


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0

print(f"Resultado é: {result:.2f}")

""" 
Este código Python solicita dois números e uma operação ao usuário, realiza a operação escolhida (adição, subtração, multiplicação ou divisão) e exibe o resultado com duas casas decimais. Se a operação inserida não for válida, exibe uma mensagem de erro.
"""

""" 
Esse código em Python é um simples programa de calculadora que solicita dois números e uma operação (+, -, *, /) ao usuário. Depois, ele realiza a operação escolhida e exibe o resultado com duas casas decimais.

Aqui está uma explicação mais detalhada:

1. **Entrada de dados:**
   - `num1` e `num2` são variáveis que armazenam os números inseridos pelo usuário. O `float(input(...))` é usado para garantir que os números sejam tratados como decimais.

2. **Escolha da operação:**
   - `operation` é uma variável que armazena a operação desejada pelo usuário. Isso é feito através da entrada fornecida pelo usuário usando `input`.

3. **Condições de controle de fluxo:**
   - O programa usa uma série de declarações `if`, `elif` (abreviação de "else if") e `else` para determinar qual operação realizar.
   - Se a operação for "+", ele realiza uma adição (`num1 + num2`).
   - Se a operação for "-", realiza uma subtração (`num1 - num2`).
   - Se a operação for "*", realiza uma multiplicação (`num1 * num2`).
   - Se a operação for "/", realiza uma divisão (`num1 / num2`).
   - Se a operação não for nenhuma das esperadas, imprime "Operação inválida" e define o resultado como 0.

4. **Saída de dados:**
   - O resultado é então exibido usando `print(f"Resultado é: {result:.2f}")`, onde `:.2f` formata o número para exibir duas casas decimais.

Em resumo, o código permite que o usuário insira dois números e escolha uma operação matemática, realizando então o cálculo desejado e exibindo o resultado.

"""
