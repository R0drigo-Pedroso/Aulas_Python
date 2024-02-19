import hashlib

# 1 - Verificar os algoritmois disponiveis

print(hashlib.algorithms_available)

# 2 - Algoritmos disponiveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
alorithm = hashlib.sha256()
print(alorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
alorithm.update(message)
print(alorithm.hexdigest())

# 4 - Utilizando o md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())