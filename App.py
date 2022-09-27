import cabecalho
import menu
import os
import base
import operacoes

res = 'Y'

while(res == 'Y' or res == 'y'):
    os.system('cls')
    cabecalho.headers.login()
    senha = input("Digite o PIN:")
    dados = base.contas().checkSenha(senha)

    if(dados==None):
        print("PIN errado, Tente Novamente!")
    else:
        os.system('cls')
        cabecalho.headers.main()
        menu.menus.main()
        op = int(input("Escolhe a operação Desejada:"))
        if(op == 1):
            os.system('cls')
            cabecalho.headers.levantameto()
            operacoes.levantamento(dados).levantar()
            res = input('Deseja continuar (Y/N):')
        elif(op == 2):
            os.system('cls')
            cabecalho.headers.consulta()
            operacoes.consultar(dados)
            res = input('Deseja continuar (Y/N):')
        elif(op == 3):
            print("Transferência")
        elif(op == 4):
            print("Deposito")
        else:
            print("sair...")


