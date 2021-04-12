import time
#O input precisa ser feito utilizando ponto e não virgula.
def fun_intro():
 print ("Olá vamos calcular o seu IMC")

def fun_calc():
 altura = float(input('Digite sua Altura: '))
 peso = float(input('Digite seu Peso: '))
 resultado = peso / (altura*altura) 
 print('Seu imc: ', resultado)
 if resultado<16:
  print('Baixo peso Grau III')

 if resultado >= 16 and resultado <= 16.99:
  print('Baixo peso grau II')
 
 if resultado >= 17 and resultado <= 18.49:
  print('Baixo peso grau I')

 if resultado >= 18.5 and resultado <= 24.99:
  print('Peso Ideal')

 if resultado >= 25 and resultado <= 29.99:
  print('Peso Ideal')

 if resultado >= 30 and resultado <= 34.99:
  print('Obesidade Grau I')
 
 if resultado >= 35 and resultado <= 39.99:
  print('Obesidade Grau II')

 if resultado > 40: 
  print('Obesidade Grau III')

fun_intro()
fun_calc()

time.sleep(30)
