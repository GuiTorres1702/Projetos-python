



class vendas: 
    def __init__(usuario,compra,venda,confirmação,self):
        self.usuario = usuario
        self.compra = compra
        self.venda = venda
        self.confirmação = confirmação
    def produto(self,produto_confirmado):
        if produto_confirmado == True:
            print('a sua compra foi aceita!')
        else: 
            print('efetue para continuar!')
        

b = int(input("coloque 1 ou 0: "))
print(vendas.produto(None,b))