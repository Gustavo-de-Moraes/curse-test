from datetime import datetime,date

hoje = datetime.now()
print("Data atual: {}".format(hoje))

  
# estrutura para mostrar a tabuada com while
while True:
  print("=-"*30)
  print("TABUADA")
  print("=-"*30)
  usu = int(input("Digite um numero: "))

# se o numero for negativo o programa é encerrado
  if usu <= 0:
    print("O numero que voce digitou foi negativo")
    break

# Codigo para mostra toda a tabuada do numero
  n1 = 0
  while n1 <= 10:
    print(usu,"X",n1,"=",usu*n1)
    n1 += 1

