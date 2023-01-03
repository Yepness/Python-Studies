#import das bibliotecas matplotlib e numpy:
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

x = np.arange(-10,10,0.1) #Delimitando intervalo de -10 a 10 para o eixo X.

#Funções:
y1 = 2*np.sin(x/2) 
y2 = 2*np.sin(2*x)
y3 = 1+np.sin(2*x)

plt.plot(x,y1,"b")  #Função 1 "blue"
plt.plot(x,y2,"c")  #Função 2 "cyan"
plt.plot(x,y3,"r")  #Função 3 "red"

plt.title("Funções") #Título 
plt.grid() #Grade
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
