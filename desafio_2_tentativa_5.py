from PIL import Image
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: converter a coordenada x de cada pixel verde em texto
pixels = image.getdata()
output = ''
output_mod_255 = ''
for i in range(len(pixels)):

    if is_pixel_green(pixels[i], 100):
        x = i % width

        # converter a coordenada x em texto
        output += chr(x)
        output_mod_255 += chr(x % 255)
    
print('Resultado das coordenadas X convertidas em texto ascii: ')
print(output)
print()
print('Resultado das coordenadas X convertidas em texto ascii mod 255: ')
print(output_mod_255)

        