from carro import Carro
from moto import Moto

def main():
    print('Carros:')
    carro_01 = Carro('Ford', 'Maverick', 2)
    carro_02 = Carro('Fiat', 'Uno', 4)
    carro_03 = Carro('Volkswagen', 'Saveiro', 4)

    print(carro_01)
    print(carro_02)
    print(carro_03)
    print()

    print('Motos:')
    moto_01 = Moto('Honda', 'Hornet 500', 'Esportiva')
    moto_02 = Moto('Honda', 'Elite 125', 'Casual')
    moto_03 = Moto('Suzuki', 'HAYABUSA', 'Esportiva')

    print(moto_01)
    print(moto_02)
    print(moto_03)

if __name__ == '__main__':
    main()
