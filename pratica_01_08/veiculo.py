class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'{self.marca.ljust(25)} | {self.modelo.ljust(25)} | {self.ligado}'

    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'

