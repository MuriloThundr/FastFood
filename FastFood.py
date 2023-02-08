print('1- Hambúrguer - R$10,00')
print('2- Batata Frita - R$5,00')
print('3- Refrigerante - R$4,00')
print('4- Sorvete - R$2,00')

pedido = int(input('Digite o n° da opção desejada: '))
quantidade = int(input('Digite a quantidade desejada: '))
nome = str(input('Digite o seu nome: '))

if pedido == 1:
    print('Hambúrger sendo preparado para ', nome)
    print('Tempo de esper de 15 minnutos.')
    total = quantidade * 10
    print('Total: R$', total)
 
