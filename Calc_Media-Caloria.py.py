import time

def intro():
 print("Olá vamos calcular o valor total de calorias consumidas hoje\n !Instruções! \n |Primeiro você digitará a quantidade de alimentos| \n |Depois quantas calorias possui cada alimento| ")

def calc_caloria():
 caloria_total = 0.0
 num_alimentos = int(input("Digite quantos alimentos você consumiu hoje: ")) 
 for x in range(num_alimentos):
  caloria_alimento = float(input("Digite quantas calorias possui o alimento: "))
  caloria_total = caloria_total + caloria_alimento

 print("Quantidade total de calorias consumida hoje: {} ".format(caloria_total))


intro()
calc_caloria()
time.sleep(30)