#Pablo Vinicius Oliveira

import numpy 
import io
import pandas as pd

x = input()
df = pd.read_csv(x)

vel1 = df['Velocidade do Vento {m/s}'].mean()
den = df['Densidade do ar {kg/m3}'].max()
ent = df['Entalpia {BTU/LB}'].min()
dir = df.query('Dia == 5 and Mes == 1')['Direcao do Vento {graus}'].mean()
pto = len(df.query('17 <= `T. Pto Orvalho {C}` <= 18'))
vel2 = df.groupby('Mes')["Velocidade do Vento {m/s}"].median()
r1 = len(df.query('`Rad Direta Normal {Wh/m2}` >= 200 and 0 < `Rad Difusa Horizontal {Wh/m2}` <= 100 '))
r2 = df.query('`Rad Direta Normal {Wh/m2}` >= 200 and 0 < `Rad Difusa Horizontal {Wh/m2}` <= 100 ')[['Mes','Dia','Hora','Rad Direta {Wh/m2}']]

print(f"Media da velocidade do vento: {vel1:.2f} m/s")
print(f"Maxima densidade do ar: {den:.2f} kg/m3")
print(f"Entalpia minima: {ent:.2f} btu/lb")
print(f"Media da direcao do vento no dia 5 do mes 1: {dir:.2f} graus")
print(f"Quantidade de registros de ponto de orvalho entre 17 e 18 graus Celsius: {pto}")
print(f"{vel2}")
print("Rad Direta Normal maior ou igual a 200 e horizontal menor ou igual a 100 e maior que zero")
print(f"Quantidade: {r1}")
print("10 primeiros:")
print(r2[0:10])
