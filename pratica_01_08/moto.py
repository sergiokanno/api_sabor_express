from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f'{self.marca.ljust(25)} | {self.modelo.ljust(25)} | {self.ligado.ljust(25)} | {self.tipo}'

