from PIL import Image
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# objetivo é somar todos os indices em 1D e tentar converter
# em algo relevante utilizando ascii ou substituicao a=1, b=2...

# variavel que guarda a soma de todas as coordenadas
soma = 0

# lista que guarda todos os pixels
pixels = image.getdata()

# loop para percorrer todos os pixels
for i in range(len(pixels)):
    # se o pixel for verde (helper function em utils.py)
    if is_pixel_green(pixels[i], 100):
        soma += i

print(f'A soma total das coordenadas: {soma}')


# podemos definir uma funcao que faca isso de maneira facil e repetitiva
def int_to_text(number, length_bit_sequence):

    # convertendo para representacao binaria
    binary_representation = format(number, 'b')

    # checar se a mensagem precisa de padding
    while len(binary_representation) % length_bit_sequence != 0:
        binary_representation = '0' + binary_representation

    i = 0
    output_add_65 = ''
    output_ascii  = ''
    bit_sequence = ''
    for bit in binary_representation:
        bit_sequence += bit
        i += 1

        if i == length_bit_sequence:
            # converte os bits em um caracter
            output_add_65 += chr(int(bit_sequence, 2) + 65)
            output_ascii += chr(int(bit_sequence, 2))
            i = 0
            bit_sequence = ''

    return output_add_65, output_ascii

# podemos percorrer de 5 em 5 bits ja que possuimos 26 letras no alfabeto
# e 2ˆ5 = 32 eh a menor potencia de 2 que pode guardar todos os bits
output_add_65, output_ascii = int_to_text(soma, 5)
print(f'Resultado do algortimo para 5 bits + 65: {output_add_65}')
print(f'Resultado do algortimo para 5 bits -> ascii: {output_ascii}')

# tentando fazer o mesmo mas dessa vez para 8 bits
output_add_65, output_ascii = int_to_text(soma, 8)
print(f'Resultado do algortimo para 8 bits + 65: {output_add_65}')
print(f'Resultado do algortimo para 8 bits -> ascii: {output_ascii}')


