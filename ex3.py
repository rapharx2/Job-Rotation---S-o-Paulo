import json

file = open('dados.json')
dados = json.load(file)

dias = 0
somaValor = 0
maiorValor = dados[0]['valor']
menorValor = dados[0]['valor']
for registro in dados:
    if registro['valor'] != 0:
        dias += 1
    somaValor += registro['valor']
    if registro['valor'] > maiorValor: 
        maiorValor = registro['valor']
    if registro['valor'] < menorValor:
        menorValor = registro['valor']

mediaValor = somaValor / dias 
diasAcimaDaMedia = 0

for registro in dados:
    if registro['valor'] > mediaValor:
        diasAcimaDaMedia += 1

#Dia com o maior valor
print(maiorValor, end="\n\n")
#Dia com o menor valor
print(menorValor, end="\n\n")
#Dias acima da media 
print(diasAcimaDaMedia, end="\n\n")

file.close()
