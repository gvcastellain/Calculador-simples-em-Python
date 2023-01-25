print("\n******************* Calculadora *******************")

soma = print('1 -- soma ')
subtracao = print('2 -- subração ')
multiplicacao = print('3 -- multiplicação ') 
divisao = print('4 -- divisão \n')


selecionar = int(input('escolha uma operação: '))


if selecionar == 1 :
    print('você escolheu soma + \n ')
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: ')) 
    resultado = n1 + n2
    print('a soma é:', resultado)


if selecionar == 2:
    print('você escolheu subtração - \n')
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    resultado = n1 - n2
    print('a subtração é: ', resultado)


if selecionar == 3:
    print('você escolheu multiplicação * \n ')
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    resultado = n1 * n2
    print('a multiplicação é: ', resultado)


if selecionar == 4:
    print('você escolheu divisão / \n')
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    resultado = n1 / n2
    print('a divisão é: ', resultado)        

else:
    print('\nessa opção não é válida \n ')