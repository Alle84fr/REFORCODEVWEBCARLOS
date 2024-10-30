#74 tupla

# criar programa que gera 5 n° aleatórios e colocar em uma tupla 
# mostrar a listagem de números gerados e o índice do menor ao maior

# lembrar que para comentar várias linhas de uma vez é só usar ctrl;

tupla = []
n = 0
while n<5:
   valor = float(input("Digite quaquer valor: "))
   tupla.append(valor)
   n += 1
print(sorted(tupla))
print(".," *15)
# fiz errado o correto é usar randit - fiz com while ao invéz de por randit repitido várias vezes -> n = (randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
from random import randint

tupla = []
for n in range(5):
   n = randint(1,20)
   tupla.append(n)
n = sorted(tupla)
print(n)
print(f"\n o menor valor é {n[0]} e o maior é {n[-1]}")