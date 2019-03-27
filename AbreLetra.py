import json
import numpy as np
from pprint import pprint
import os
from tensorflow.python.autograph.pyct import origin_info


path_to_file = "ptbr-eng/baseletras.json"
with open(path_to_file) as f:
    data = json.load(f)

#pprint(data)
json_data = []
originais = []
traduzidas = []
tamanho = np.count_nonzero(data)
#print(tamanho)
#print(data[1])

for x in range(0, tamanho):
    json_data.append(data[x])
    if ('Traduzido' in data[x].keys()):
        traduzidas.append(data[x]['Traduzido'])
    if('Original' in data[x].keys()):
        originais.append(data[x]['Original'])

    
print(traduzidas[1090])
print(originais[1090])
##print(json_data[0][0])
print("ORIGINAL")
print(np.count_nonzero(originais))
print("TRADUZIDA")
print(np.count_nonzero(traduzidas))
print(np.count_nonzero(json_data))




listaoriginal = []
listatraduzida = []
tamanho = np.count_nonzero(originais)


for x in range(0, tamanho):
    tamanhointerno = np.count_nonzero(originais[x])
    espelho = np.count_nonzero(traduzidas[x])
    if (tamanhointerno == espelho):
        for y in range(0, tamanhointerno):
            if(originais[x][y] != ' ' or traduzidas[x][y] != ' '):
                listaoriginal.append(originais[x][y])
                listatraduzida.append(traduzidas[x][y])

#print(listaoriginal)
print("LISTA ORIGINAL")
print(np.count_nonzero(listaoriginal))
#print(listaoriginal[0])
#print(listatraduzida[70])
print("LISTA TRADUZIDA")
print(np.count_nonzero(listatraduzida))

novo = open("ptbr-eng/ptbr-en-3000.txt", "x")
novo = open("ptbr-eng/ptbr-en-3000.txt", "w")
tamanho = np.count_nonzero(listaoriginal)
tamanho = 3000
for x in range(0, tamanho):
    novo.write(listaoriginal[x])
    novo.write('\t')
    novo.write(listatraduzida[x])
    novo.write('\n')
