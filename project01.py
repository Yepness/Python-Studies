# Nome: Pablo Vinicius Oliveira 

import math

valor = float (input("Quando voce nasceu? "))
idade = int (2022 - valor)
if idade <= 12:
  print ("você tem " + str(idade), "anos e, portanto, e criança.")
elif idade >= 13 and idade <= 17:
  print ("você tem " + str(idade), "anos e, portanto, e adolescente.")
elif idade >= 18 and idade <= 64:
  print ("você tem " + str(idade), "anos e, portanto, e adulto.")
else:
  print ("você tem " + str(idade), "anos e, portanto, e experiente.")
