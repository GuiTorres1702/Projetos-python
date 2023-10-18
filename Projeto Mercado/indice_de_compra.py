import pandas as pd 

# 'r' -> usado ler arquivos txt
# 'w' -> usado somente para escrever txt
# 'r+' usado para ler e escrever txt
# 'a' -> usado para acrescentar txt



#with open('valores_de_mercado.txt','r') as arquivo:
#    for valor in valores_de_mercado:
#       arquivo.write(str(valor) + '\n')

tabela = pd.read_excel("Pasta.xlsx")
difir = pd.DataFrame(tabela)
print(difir)