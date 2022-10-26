# Nome: Pablo Vinicius Oliveira 

import math

v = (input(""))
if v.isnumeric():
  x = int(v)
  print(math.factorial(x))
elif v == "ufabc":
  print("minha universidade")
else:
  print(v)
