# 1 - Função de potência de número
def power(num): return num ** 2


# 2 - Função que verifica se o npumero é par
def pair(x): return x % 2 == 0


# 3 - Função que divide um número por outro
def divNum(x, y): return x / y


# 4 - Função que inverte uma string
def reverse(s): return s[::-1]


print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10, 2))
print(divNum(6, 2))
print(reverse("Python"))
print(reverse("JavaScript"))
