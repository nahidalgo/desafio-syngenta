from PIL import Image
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# esta tentativa tem o intuito de converter cada coordenada
# em 1D, ou seja, o indice do pixel no vetor 1D da imagem
# em um caracter da tabela ASCII ou utf-8

# string que guarda todos os caracteres gerados usando a func chr()
output = ''

# string que guarda todos os caracteres gerados usando a func chr() e mod % 255
output_mod_255 = ''

# lista que guarda todos os pixels
pixels = image.getdata()

# loop para percorrer todos os pixels
for i in range(len(pixels)):
    # se o pixel for verde (helper function em utils.py)
    if is_pixel_green(pixels[i], 100):
        # salva a coordenada em i e realiza as conversoes
        output += chr(i)
        output_mod_255 += chr(i % 255)
    
print('A saida para o indice dos pixels em 1D resulta em para ASCII:')
try :
    print(output)
except:
    print('Uma excecao ocorreu devido a caracteres invalidos')

print()

print('A saida para o indice dos pixels em 1D com resto de 255 resulta em')
try :
    print(output_mod_255)
except:
    print('Uma excecao ocorreu devido a caracteres invalidos')
