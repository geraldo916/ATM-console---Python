import menu
import base

class levantamento:
    def __init__(self,dados):
        self.dados = dados
        self.saldo = base.contas.conta['saldo']
        self.opcoes = [2000.00,5000.00,10000.00,25000.00,30000.00,45000.00]

    def levantar(self):
        menu.menus.levantameto()
        op = int(input('Insira a opção desejada:'))
        resultado = 0
        valor = 0
        if(op==7):
            valor = float(input('Insira o valor desejado:'))
            resultado = self.saldo - valor
        elif(op==8):
            pass
        else:
            valor = self.opcoes[op-1]
            resultado = self.saldo - valor
        
        if(resultado<0):
            print('Saldo Insuficiente')
        else:
            base.contas.conta['saldo'] = resultado
            print("Saldo na conta: {}".format(self.dados['saldo']))

class consultar:
    def __init__(self,dados):
        print("Saldo:",dados['saldo'])   