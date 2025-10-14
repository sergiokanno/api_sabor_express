from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

napolitano = Sobremesa('Napolitano', 32.0, 'Sorvete', 'Pote Grande', 'Sorvete Napolitano')
restaurante_praca.adicionar_no_cardapio(napolitano)
print(f'{'Nome'.ljust(25)} | {'Tipo'.ljust(25)} | {'Tamanho'.ljust(25)} | {'Descricao'.ljust(25)} | {'Preço'}')
print(napolitano)
print()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
