# programa e comandos simples para data e calendario
# bibliotecas
from datetime import datetime, date
import calendar

#variaveis
hoje = datetime.now()
ano = int(input("digite o ano atual: "))
mes = int(input("digite o mes atual: "))
dia_semana = calendar.weekday(2026, 8, 19)
a = calendar.isleap(ano)

# comandos
print("\n",calendar.month(ano,mes)) # mostra somente o mes e o ano
print("Dia da semana:",dia_semana)# Obter o dia da semana de uma data
print("é bissexto?",a) # mostra se o ano é bisexto
print("Data atual: {}".format(hoje)) # mostra a data atual

