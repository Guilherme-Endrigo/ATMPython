class Conta:

    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo_inicial
        self.__ativa = False
        self.__operacoes = [('saldo inicial', saldo_inicial)]

    # acesso de propriedades

    @property
    def titular(self):
        return self.__titular

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, situacao):
        if not self.ativa:
            self.__ativa = situacao
            print("A conta de " + self.titular + " foi ativada")
        else:
            self.__ativa = False
            print("essa conta de " + self.titular + " foi desativada")

    # metodo estatico

    @staticmethod
    def sobre_banco():

        dados_banco = ("Banco Itaú Unibanco", "Itaú", "PRIVADO", "www.itau.com.br")
        resposta = ""

        while not resposta == "Y" or not resposta == "N":
            resposta = input("Deseja saber mais informações sobre o banco? Y/N: ")
            resposta = resposta.upper().strip()
            if resposta == "Y":
                print(dados_banco)
                print(resposta)
            elif resposta == "N":
                print("Ok, volte sempre")
            else:
                print("digite uma opção valida")

    # metodos de uso

    def tirar_extrato(self):
        print(self.__operacoes)
        print("Seu saldo atual é: " + str(self.__saldo))

    def __pode_receber(self, valor):
        if self.__ativa and valor > 0:
            return True
        else:
            return False

    def __pode_retirar(self, valor):
        if self.__saldo - valor >= 0 and self.__ativa and valor > 0:
            return True
        else:
            return False

    def depositar(self, valor):
        if self.__pode_receber(valor):
            self.__saldo += valor
            operacao_realizada = ('deposito', valor)
            self.__operacoes.append(operacao_realizada)

    def sacar(self, valor):
        if self.__pode_retirar(valor):
            self.__saldo -= valor
            operacao_realizada = ('saque', valor)
            self.__operacoes.append(operacao_realizada)

    def transferir(self, conta_destino, valor):
        if conta_destino.__pode_receber(valor) and self.__pode_retirar(valor):
            self.sacar(valor)
            conta_destino.depositar(valor)
            operacao_realizada = ('transferencia', valor)
            self.__operacoes.append(operacao_realizada)
