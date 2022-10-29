# Python-Studies
Repository for the study of optional Python projects.

Project Description 01:

Desenvolvimento de um programa que leia um número inteiro da entrada. Esse número representa o ano de nascimento de uma pessoa. Assumindo que estamos em 2022 e o aniversário da pessoa já passou, escreva uma frase como a seguinte na saída (não vamos usar acentos):

Voce tem X anos e, portanto, e Y.

X é a idade da pessoa, Y é uma palavra de acordo com os critérios abaixo:
Y = "crianca" se X for menor ou igual a 12;
Y = "adolescente" se X for maior ou igual a 13 e menor ou igual a 17;
Y = "adulto" se X for maior ou igual a 18 e menor ou igual a 64;
Y = "experiente" se X for maior ou igual a 65.
Exemplos:
Se o valor lido for 2015, deve-se escrever "Voce tem 7 anos e, portanto, e crianca."
Se o valor lido for 1980, deve-se escrever "Voce tem 42 anos e, portanto, e adulto."
Se o valor lido for 1900, deve-se escrever "Voce tem 122 anos e, portanto, e experiente."

//========================================================================================================

Project Description 02:

Desenvolvimento de um programa que leia uma string da entrada e escreva na saída uma das opções abaixo:
Se a string representa um número inteiro, escreva o fatorial desse número na saída;
Se a string for "ufabc", escreva "minha universidade" na saída;
Se a string não representa um número inteiro nem é "ufabc", escreva a própria string na saída.

Exemplos:
Para entrada "4", a saída deve ser "24"
Para entrada "ufabc", a saída deve ser "minha universidade"
Para entrada "BCC", a saída deve ser "BCC"

//========================================================================================================

Project Description 03:

Desenvolvimento de um programa que leia os seguintes dados da entrada:
Uma cadeia de caracteres F;
Um número decimal A representando o início de uma sequência;
Um número decimal B representando o fim de uma sequência;
Um número decimal C representando um incremento.
Use os valores A, B, e C como parâmetros da função arange da biblioteca numpy e guarde o resultado em uma variável L. Depois, faça uma das operações seguintes:

Se F="seno", use a biblioteca numpy para calcular o seno de todos os números de L, e armazene esse resultado em uma lista R;
Se F="cosseno", use a biblioteca numpy para calcular o cosseno de todos os números de L, e armazene esse resultado em uma lista R;
Se F="log10", use a biblioteca numpy para calcular o logaritmo na base 10 de todos os números de L, e armazene esse resultado em uma lista R;
Se F="log2", use a biblioteca numpy para calcular o logaritmo na base 2 de todos os números de L, e armazene esse resultado em uma lista R;
Por fim, use a função print para escrever os valores na lista R na saída. Os valores devem ser impressos separados por espaço, na mesma ordem em que estão na lista. Se o valor de F for inválido, escreva "funcao desconhecida" e termine o programa.

//========================================================================================================

Project Description 04:

O objetivo deste trabalho é usar a biblioteca pandas do Python para analisar arquivos CSV com dados de diferentes cidades brasileiras disponibilizados pelo Laboratório de Eficiência Energética em Edificações. Cada arquivo CSV representa uma cidade, e cada linha tem dados de medições de diversas métricas organizados por mês, dia, e hora de coleta. Neste trabalho, você criará um programa que lê um arquivo CSV, e, partir da leitura, irá informar diversos dados na tela.

Entrada do programa: o único valor a ser lido é o nome do CSV a ser processado.

Saída: os seguintes dados deverão ser impressos na saída, nesta ordem:

Uma frase do tipo "Media da velocidade do vento: X.XX m/s", em que X.XX é média de todas as medidas de velocidade do vento do arquivo. Esse valor deve ser apresentado aproximado para duas casas decimais;
Uma frase do tipo "Maxima densidade do ar: X.XX kg/m3", em que X.XX é o maior valor entre todas medidas de densidade do ar do arquivo. Esse valor deve ser apresentado aproximado para duas casas decimais;
Uma frase do tipo "Entalpia minima: X.XX btu/lb", em que X.XX é o menor valor entre todas medidas de entalpia do arquivo. Esse valor deve ser apresentado aproximado para duas casas decimais;
Uma frase do tipo "Media da direcao do vento no dia 5 do mes 1: X.XX graus", em que X.XX é média das medidas de direção do vento do arquivo coletadas no dia 5 do mês 1. Esse valor deve ser apresentado aproximado para duas casas decimais;
Uma frase do tipo "Quantidade de registros de ponto de orvalho entre 17 e 18 graus Celsius: XXX", em que XXX a quantidade inteira de linhas do arquivo em que o ponto de orvalho está no intervalo de 17 e 18 graus Celsius (incluindo os valores 17 e 18);
Faça um groupby para obter todas as medianas de velocidade do vento agrupadas por mês. Passe o resultado da função groupby para a função print;
A frase "Rad Direta Normal maior ou igual a 200 e horizontal menor ou igual a 100 e maior que zero"
Faça uma busca para encontrar todas linhas cujo campo "Rad Direta Normal" seja maior ou igual a 200 e cujo campo "Rad Difusa Horizontal" seja menor ou igual a 100 e maior que zero. Usando a busca, escreva uma frase do tipo "Quantidade: XXX", em que XXX é um inteiro com a quantidade de registros nessa busca. Depois imprima a frase "10 primeiros:". Por fim, faça um filtro dessa busca para obter somente os campos mês, dia, hora, e rad direta. Então use a função print para imprimir os dez primeiros registros do filtro.
