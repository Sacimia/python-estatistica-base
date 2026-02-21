#Referencia de Prof. Francisco Rodrigues (Youtube - Introdução a Teoria das Probabilidades)

import numpy as np

p = 0.6
nsim = 10
nhead = 0
saida = []

for i in range(nsim):  # agora roda 10 vezes
    if np.random.uniform() < p:
        nhead += 1
        saida.append(1)
    else:
        saida.append(0)

print('Saída:', saida)
print('Probabilidade de sair cara:', nhead/nsim)
print('Probabilidade de sair coroa:', 1 - nhead/nsim)