class Carro:
    def __init__(self, marca, cor, modelo, motor, ano, preco): # método só funciona dentro da classe
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.motor = motor
        self.ano = ano
        self.preco = preco

    def getMarca(self):
        return self.marca

    def getCor(self):
        return self.cor

    def getModelo(self):
        return self.modelo

    def getMotor(self):
        return self.motor

    def getAno(self):
        return self.ano

    def getPreco(self):
        return self.preco


def main():
    # automovel = []
    marca = input("Digite a marca: ")
    cor = input("Digite a cor: ")
    modelo = input("Digite o modelo: ")
    motor = input("Digite o motor: ")
    ano = input("Digite o ano: ")
    preco = input("Digite o preco: ")
    automovel = Carro(marca, cor, modelo, motor, ano, preco)
    print(automovel.getMarca(), automovel.getCor(), automovel.getModelo(), automovel.getMotor(), automovel.getAno(), automovel.getPreco())


main()
