import time
def intro():
 print("Olá vamos jogar um jogo de Fibonacci")

def jogo():
 a = 0
 b = 1
 num_escolhido = int(input("Digite um número inteiro"))

 while b < num_escolhido: 
  a, b = b, a+b 

 if b != num_escolhido or num_escolhido == 0:
  print("Ação Falho")
 else:
  print("Ação Bem sucedida")

 print("Você escolheu o: {}".format(num_escolhido))

intro()
jogo()

time.sleep(30)
