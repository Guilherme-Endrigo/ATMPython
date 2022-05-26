import conta_bancaria

contaOperação = conta_bancaria.Conta("guilherme", 21, 55, 100)
contaParatranferencia = conta_bancaria.Conta("Mario", 21, 55, 100)


def menu_bancario():
    print("********* Caixa Eletronico *********")
    print()
    print("|------------ MENU ----------------|")
    print("| 1- Extrato                       |")
    print("| 2- Saque                         |")
    print("| 3- Deposito                      |")
    print("| 4- Transferencia                 |")
    print("| 5- Sobre                         |")
    print("| 6- Ativar a conta                |")
    print("| 7- sair                          |")
    print("|----------------------------------|")
    print()

    operacao = input("Selecione a operação desejada: ")

    while not operacao == "sair":

        if operacao == "1":
            contaOperação.tirar_extrato()
            operacao = input("Selecione a nova operação desejada: ")

        elif operacao == "2":
            valor_saque = int(input("quanto você deseja sacar? "))
            contaOperação.sacar(valor_saque)
            operacao = input("Selecione a nova operação desejada: ")

        elif operacao == "3":
            valor_deposito = int(input("qual o valor que deseja depositar? "))
            contaOperação.depositar(valor_deposito)
            operacao = input("Selecione a nova operação desejada: ")

        elif operacao == "4":
            # falta encontrar a conta
            #conta_destino = input("Para que conta você deseja transferir? ") finalizar logica
            valor_transferencia = int(input("Qual o valor que você deseja transferir? "))
            contaOperação.transferir(contaParatranferencia, valor_transferencia)
            operacao = input("Selecione a nova operação desejada: ")

        elif operacao == "5":
            conta.sobre_banco()
            operacao = input("Selecione a nova operação desejada: ")

        elif operacao == "6":
            contaOperação.ativa = True

        elif operacao == "7":
            print("Agradecemos sua preferencia")
            operacao = "sair"

        else:
            print("Operação invalida")
            operacao = input("Selecione a operação desejada: ")

if (__name__ == "__main__"):
    menu_bancario()

