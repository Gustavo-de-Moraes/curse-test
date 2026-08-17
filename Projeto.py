from datetime import datetime,date # biblioteca para data
hoje = datetime.now()

print(hoje)

op = 0
# introdução do programa
print("=-"*30)
print("CONVERSOR DE DINHEIRO")
moeda = float(input("digite um valor que deseja converter: R$"))
print("[1] converter em bitcoin ₿")
print("[2] conveter em dolar U$$")
print("[3] converter em euros €")
print("[4] digitar outro valor para converter R$")
print("[5] sair do programa")
while op != 5:
  op = int(input("sua opção :"))
  if op == 1:
    dolar = 5,21 * 1 
    print("Com R${} é possivel converter {}U$$".format(moeda,dolar))
