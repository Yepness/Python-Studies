# Nome: Pablo Vinicius Oliveira 

import math
import numpy as np

F = str(input(''))
A = float(input(''))
B = float(input(''))
C = float(input(''))

L= np.arange(A,B,C) # (valor inicial, valor final, encrementos)
R= []

if F == 'seno': 
  seno = np.sin(L)
  R.append(seno)
  print(*seno, sep= " ")
elif F == 'cosseno':
  cosseno = np.cos(L) 
  R.append(cosseno)
  print(*cosseno, sep= " ") 
elif F == 'log10':
  log10 = np.log10(L)
  R.append(log10)
  print(*log10, sep= " ") 
elif F == 'log2':
  log2 = np.log2(L)
  R.append(log2)
  print(*log2, sep= " ")    
else:
  print("funcao desconhecida")
