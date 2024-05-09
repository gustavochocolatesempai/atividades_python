    #Faça um Programa que peça as 4 notas bimestrais e mostre a média.

if __name__ == '__main__':

    #pedindo a primeira media
    print('digite sua primeira nota' )
    nota1 = float(input())

    #pedindo a segunda media
    print('digite sua segunda nota' )
    nota2 = float(input())

    #pedindo a terceira media
    print('digite sua terceira nota')
    nota3 = float(input())

    #pedindo a quarta media
    print('digite sua quarta nota')
    nota4 = float(input())


    media = (nota1+nota2+nota3+nota4)/4

    #imprimindo a soma
    print(f'media: {media}')

