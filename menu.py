import calculadora

def menu():
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    return opcao

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            print(calculadora.somar(2, 2))
        elif opcao == 2:
            print(calculadora.subtrair(2, 2))
        elif opcao == 3:
            print(calculadora.multiplicar(2, 2))
        elif opcao == 4:
            print(calculadora.dividir(2, 2))
        elif opcao == 0:
            break
        else:
            print('Opção inválida!')

main()

    