#Faça um Programa que peça dois números e imprima a soma.

if __name__ == '__main__':
    # pedindo primeiro numero1


    print ("digite o primeiro numero: ")
    numero1 = int(input()) # int() converte uma string

    #pedindo o segundo numero
    print ("digite o segundo numero: ")
    numero2 = int(input())

    #fazendo a soma

    resultado = numero1 + numero2

    #imprimindo
    print(f'soma: {resultado}')
