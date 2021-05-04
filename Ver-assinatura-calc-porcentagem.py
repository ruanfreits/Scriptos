import time
#pode ser feito utilizando o switch
def intro():
 print ("Olá vamos analisar seu tipo de assinatura")
 print("Primeiro escolha seu tipo de assinatura")
 print("[1]BASIC\n[2]SILVER\n[3]GOLD\n[4]PLATINUM")
 resposta = float(input('Digite o numero da assinatura:'))
 faturamento = float(input('Digite seu faturamento'))
 
 if resposta == 1:
  bonus = (faturamento * 30)/ 100
  print("Seu bonus é de: R$",bonus)

 if resposta == 2:
  bonus = (faturamento * 20)/ 100
  print("Seu bonus é de: R$",bonus)

 if resposta == 3:
  bonus = (faturamento * 10)/ 100
  print("Seu bonus é de: R$",bonus)

 if resposta == 4:
  bonus = (faturamento * 5)/ 100
  print("Seu bonus é de: R$",bonus)

intro()
time.sleep(30)
