import numpy as np

notas = np.array([5,6,4,8,7,6,5,9,2,5,7,5])

media = np.mean(notas)

print(media)

desvio_padrao = np.std(notas)

print(desvio_padrao)

notas_prova1 = np.array([5,6,4,8,7,6])

notas_prova2 = np.array([5,9,2,5,7,5])

correlacao = np.corrcoef(notas_prova1, notas_prova2)

print(correlacao)
