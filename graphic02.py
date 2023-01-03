import numpy as np #Funções da numpy.
# CSV (Comandos Separados por Vírgulas)
import io
import pandas as pd #(Biblioteca para lidar com CSV)
import matplotlib.pyplot as plt
%matplotlib inline
from google.colab import files #importação do arquivo CSV.
arquivos = files.upload()

#Definão de váriaveis:
_list = ['PETR4.csv']
_name = str(input("Qual o nome do CSV? "))

if (_name in _list):
  df = pd.read_csv(io.BytesIO(arquivos["PETR4.csv"]));

  x = np.arange(0,4999,1);
  y1 = df[::-1]["Último"].str.replace(',','.').astype(float); #Trocar as ',' da tabela por '.' para o cálculo.
  (a,b)=np.polyfit(x = np.arange(0,4999,1) ,y = y1, deg = 1);
  y2 = a*x+b;

  plt.plot(x,y1,"b") #Plotar os valores referente ao arquivo CSV baseado em x e y1 definidos na cor azul.
  plt.plot(x,y2,"r") #Plotar os valores referente ao arquivo CSV baseado em x e y2 definidos na cor azul.

  plt.title("Valor da Ação") #Título 
  plt.grid() #Grade
  plt.xlabel("Data")
  plt.ylabel("Valor")
