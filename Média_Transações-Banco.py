import time

def saudaçao():
 print("Olá vamos analisar suas transações bancárias")

def info_trans():
 trans_total = 0.0
 num_trans = int(input("Digite o numero de transações feitas hoje: "))
 for x in range(num_trans):
  valor_trans = float(input("Digite o valor da transação: "))
  trans_total = trans_total + valor_trans

 media = trans_total/int(num_trans)
 print("A média de valor traferido é: {} ".format(media))
 print("O valor total transferido (gasto) foi: {}".format(trans_total))
saudaçao()
info_trans()
time.sleep(30)
