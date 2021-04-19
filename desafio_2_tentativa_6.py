from PIL import Image
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: converter a coordenada y de cada pixel verde em texto
pixels = image.getdata()
output = ''
output_mod_255 = ''
for i in range(len(pixels)):

    if is_pixel_green(pixels[i], 100):
        y = i // width

        # converter a coordenada y em texto
        output += chr(y)
        output_mod_255 += chr(y % 255)
    
print('Resultado das coordenadas Y convertidas em texto ascii: ')
print(output)
print()
print('Resultado das coordenadas Y convertidas em texto ascii mod 255: ')
print(output_mod_255)

# obs: aqui pode-se notar o aparecimento de um padrao interessante indicando que so ha um
# pixel verde por linha

        