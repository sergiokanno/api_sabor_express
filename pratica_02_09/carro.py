from veiculo import Veiculo

class Carro(Veiculo):

    def ligar(self):
        pass

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        return f'{self.marca.ljust(25)} | {self.modelo.ljust(25)} | {self.cor}'

