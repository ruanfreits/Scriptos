import time
segunda_num = int(input("Digite o numero de votos na segunda"))
terca_num = int(input("Digite o numero de votos na terça"))
quarta_num = int(input("Digite o numero de votos na quarta"))
quinta_num = int(input("Digite o numero de votos na quinta"))
sexta_num = int(input("Digite o numero de votos na sexta"))

if segunda_num > terca_num and segunda_num > quarta_num and segunda_num > quinta_num and segunda_num > sexta_num:
 print("sengunda é a vencedora")
 vencedor = "segunda"
elif terca_num > segunda_num and terca_num > quarta_num and terca_num > quinta_num and terca_num > sexta_num:
 print("terca é a vencedora")
 vencedor = "terca"
elif quarta_num > terca_num and quarta_num > segunda_num and quarta_num > quinta_num and quarta_num > sexta_num:
 print("quarta é a vencedora")
 vencedor = "quarta"
elif quinta_num > terca_num and quinta_num > quarta_num and quinta_num > segunda_num and quinta_num > sexta_num:
 print("quinta é a vencedora")
 vencedor = "quinta"
elif sexta_num > terca_num and sexta_num > quarta_num and sexta_num > quinta_num and sexta_num > segunda_num:
 print("Sexta Vencedora")
 vencedor = "sexta" 
else:
 print("Existiu um empate")

time.sleep(30)
