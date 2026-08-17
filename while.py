from datetime import datetime, date
import random
hoje = datetime.now()

print("data atual: {}".format(hoje))
# while é uma estrutura de repetição

c = 1
while c <= 10:
  print(c , end=" ")
  c += 1

# exemplo de projeto com estrutura while
print("\033[1;31m-----------------\033[m")
print("\033[1;31mJOGO DE ADIVINHAÇÃO\033[m")
print("\033[1;31m-----------------\033[m")

palpites = 0
n1 = int(input("digite um numero:"))
n3 = random.randint(1,10)
print("\033[1;34mNUMERO DO USUARIO {}\033[m".format(n1))
print("")#linha em branco

while n1 != n3:
    n1 = int(input("digite um outro numero:"))
    palpites += 1
    if n3 > n1 :
        print("\033[1;31m mais,tente novamente\033[m")
    else:
        print("\033[1;36m menos,tente novamente\033[m")

print("\033[1;35mPARABÉNS,VOCE ACERTOU O NUMERO {} COM {} TENTATIVAS!!!\033[m".format(n3,palpites))

# isso é um treinamento git e github

