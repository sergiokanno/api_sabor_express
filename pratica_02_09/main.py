from carro import Carro

def main():
    print(f'{'Marca'.ljust(25)} | {'Modelo'.ljust(25)} | {'Cor'}')
    carro_01 = Carro('Ford', 'Maverick', 'Azul')
    carro_02 = Carro('Fiat', 'Uno', 'Vermelho')
    carro_03 = Carro('Volkswagen', 'Saveiro', 'Cinza')

    print(carro_01)
    print(carro_02)
    print(carro_03)

if __name__ == '__main__':
    main()
