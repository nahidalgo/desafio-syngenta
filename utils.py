# arquivo que contem helper functions

def is_pixel_green(pixel, threshold):
    if pixel[1] > threshold and pixel[1] > pixel[0] and pixel[1] > pixel[2]:
        return True
    return False

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