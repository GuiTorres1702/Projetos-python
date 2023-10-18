class carro:
    id:int
    carros:str
    valor:float

    def __init__(self,id:int,carros:str,valor:float):
        self.id = id
        self.carros = carros
        self.valor = valor

def main():
    cliente = carro()
    