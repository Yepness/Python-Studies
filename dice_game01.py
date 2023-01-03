import random as rd #Biblioteca Random

p1=0;
p2=0;
vd=[1,2,3,4,5,6];

winner = False
while not winner:
  
  A=int(input("jogador 1 escolha um número inteiro entre 1 e 6: "));
  B=rd.randint(a=1,b=6)
  D=rd.choice(vd)

  if A == B or B == A:
    p1=p1;
    p2=p2;

  else:

   if A == D:
    p1=p1+1;
  
   if B == D:
    p2=p2+1;

   else:

      if D<=3:
        p1=p1+1;
  
      if D>=4:
        p2=p2+1;

  print("Valor escolhido pelo jogador 1: " + str(A), "");
  print("Valor escolhido pelo jogador 2: " + str(B), "");
  print("Valor sorteado no dado" + str(D), "");
  print("Placar de pontos atual: " "Jogador 1: " + str(p1), "Jogador 2: " + str(p2));

  if p1 == 3:
    print("Parabéns, Jogador 1")
    winner = True
  if p2 == 3:
    print("Parabéns, Jogador 2")
    winner = True
