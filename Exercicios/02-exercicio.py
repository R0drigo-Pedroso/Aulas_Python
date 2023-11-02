"""
Exercicio 2

* Subtituindo caractere repetido:
-> Escreva um programa Python para obter uma string de uma determinada string
em que todas as ocorrências de seu primeiro caractere foram alteradas para $,
exceto o pr[oprio primeiro caractere
Ex: fifa 23 -> fi$a 23

* Troca de caracteres:
-> Escreva um programa Python para obter uma única string de duas string fornecendo
seraparadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex: abc xyz -> xyc abz
"""

# Substituido caracteres repetido
name = input("Digite o nome de Jogo\n ")

char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:]
print(new_name)


# Troca de caracteres
st1 = 'cab'  # zyb
st2 = 'zyx'  # cax

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print(new_st1)
print(new_st2)
