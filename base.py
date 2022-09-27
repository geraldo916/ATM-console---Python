class contas:
    conta = {'id':1,'Conta':'25423562','propietario':'Geraldo','saldo':90000,'senha':'12345'}
    
    def checkSenha(self,senha):
        if(self.conta.get('senha') == senha):
            return self.conta