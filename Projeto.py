from datetime import datetime,date # biblioteca para data
hoje = datetime.now()

print(hoje)

op = 0
# introdução do programa
print("=-"*30)
print("CONVERSOR DE DINHEIRO")
moeda = float(input("digite um valor que deseja converter: R$"))
while op != 5:
  print("[1] converter em bitcoin ₿") 
  print("[2] conveter em dolar U$$")
  print("[3] converter em euros €")
  print("[4] digitar outro valor para converter R$")
  print("[5] sair do programa")
  op = int(input("sua opção :"))
  if op == 1: # converter para o bitcoin
    bitcoin =  moeda * 239286.02
    print("Com R${} é possivel converter {}₿".format(moeda,bitcoin))

  if op == 2: # converter para o dolar
    dolar = moeda * 0.19
    print("Com R${} é possivel converter {}U$$".format(moeda,dolar))

  if op == 3: # converter para o Euro
    euro = moeda * 0.17
    print("Com R${} é possivel converter {}€".format(moeda,euro))

  if op == 4: # adiciona novamente um valor para converter
    print("Por favor informe um novo valor para ser convertido")
    moeda = float(input("digite um valor que deseja converter R$"))
