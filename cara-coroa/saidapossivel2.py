#Sequencia de Cara e Coroa e suas Probabilidades Aleatórias

import numpy as np

p = 0.6
nsim = 10
#Gere 10 números aleatórios entre 0 e 1
resultados = np.random.uniform(size=nsim) < p 


#Se tirar o tolist vai gera a sequencia de np.int64()
#Ao não tirar o tolist, ou seja, colocar como astype(int).tolist() gere em sequencia padrao de python
saida = resultados.astype(int).tolist()

print('Saída: ', list(saida))
print('Probabilidade de sair cara: ', np.mean(saida))
print('Probabilidade de sair coroa: ', 1-np.mean(saida))