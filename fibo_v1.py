print('Programa que gera a sequência de Fibonacci (v.1)')
print('0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...')
n = int(input('Quantos termos a série terá? '))
seq = [0, 1]
aux = seq[-1]

for i in range(n-2) :
    seq.append(aux)
    aux += seq[-2]
print(seq)

# lista =[1, 10, 100, 1000, 10000]
# print('último: {}'.format(lista[-1]))
# print('penúltimo: {}'.format(lista[-2]))
# print('antepenúltimo: {}'.format(lista[-3]))
# print('anteantepenúltimo: {}'.format(lista[-4]))
# auxiliar = 3
# lista.append(auxiliar)
# print(lista)
# auxiliar = lista[-1] + lista[-2]
# lista.append(auxiliar)
# print(lista)
#
