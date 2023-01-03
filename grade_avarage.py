import math

soma = 0.0 #O valor inicial da soma sempre vai ser zero.
v1 = int(input("Qual o número total de trabalhos? "))
#for ; in lista: |(lista é a quantidade de elementos a serem executados)
#podemos usar range(inicio,fim+1porque ele ignora o ultimo + encremento)
for v2 in range(1,v1+1,1):
  nota = float(input("Qual a nota do trabalho " + str(v2) + "? "))
  soma = soma + nota

v3 = float(input("Qual a nota da prova? "))

notaf = ((soma/v2)*0.6 + v3*0.4)

if notaf <= 5:
  print("você tem " + str(notaf), "portanto conceito F.")
elif notaf >= 5 and notaf < 6:
  print("você tem " + str(notaf), "portanto conceito D.")
elif notaf >= 6 and notaf < 7:
  print("você tem " + str(notaf), "portanto conceito C.")
elif notaf >= 7 and notaf < 8.5:
  print("você tem " + str(notaf), "portanto conceito B.")
elif notaf >= 8.5 and notaf <= 10:
  print("você tem " + str(notaf), "portanto conceito A.")
