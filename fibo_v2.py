print('Programa que gera a sequência de Fibonacci (v.2)')
print('0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...')
n = int(input('Quantos termos a série terá? '))
if n == 0 or n == 1 :
    print('0')
elif n == 2 :
    print('0')
    print('1')
else :
    penultimo = 1
    ultimo = 1
    aux = 1
    i = 3
    print(penultimo - 1)
    print(penultimo)
    print(ultimo)
    while i < n :
        aux = ultimo
        ultimo = aux + penultimo
        penultimo = aux
        print(ultimo)
        i += 1
# raciocínio:
# a variável 'aux' é usada para guardar o valor da variável 'último'
# e gerar o próximo termo da série na soma com a variável 'penúltimo'
#
