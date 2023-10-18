import pyodbc
def conecta_ao_banco(driver='SQL Server Native Client 19.0',server='GUILHERMETORRES\SQLEX',database='master',usarname=None,password=None,trust_connection='yes'):
    string_conexao  = f"DRIVER={driver};SERVER={server};DATABASE{database};UID={usarname};PWD{password};TRUST_CONNECTION={trust_connection}"

    conexao = pyodbc.connect(string_conexao)



class taxar:
       
    def __init__(self, produto, valor, taxa):
        self.produto = int(produto)
        self.valor = float(valor)
        self.taxa = float(taxa)
        
    
    def mostrar_resultados(self):
        print(self.produto,self.valor, self.taxa)
        
               
    
