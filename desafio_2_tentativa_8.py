from PIL import Image
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: converter a subtracao de x e y de cada pixel verde em texto
pixels = image.getdata()
output = ''
output_mod_255 = ''
output_inverse = ''
output_inverse_mod_255 = ''
for i in range(len(pixels)):

    if is_pixel_green(pixels[i], 100):
        x = i % width
        y = i // width

        try:
            output += chr(x-y)
        except:
            output += ''
        try:
            output_mod_255 += chr((x - y) % 255)
        except:
            output_mod_255 += ''
        try:
            output_inverse += chr(y-x)
        except:
            output_inverse += ''
        try:
            output_inverse_mod_255 += chr((y-x) % 255)
        except:
            output_inverse_mod_255 += ''
        
print()
print('Resultado das coordenadas X-Y convertidas em texto ascii: ')
print(output)
print()
print('Resultado das coordenadas X-Y convertidas em texto ascii mod 255: ')
print(output_mod_255)
print()
print('Resultado das coordenadas Y-X convertidas em texto ascii: ')
print(output_inverse)
print()
print('Resultado das coordenadas Y-X convertidas em texto ascii mod 255: ')
print(output_inverse_mod_255)

        