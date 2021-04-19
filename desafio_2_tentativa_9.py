from PIL import Image
from utils import is_pixel_green
import collections

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: gerar a lista de frequencia para as coordenadas x dos pixels verdes
pixels = image.getdata()
# lista que armazena todas as coordenadas x de cada pixel verde
x_coordinates = []
for i in range(len(pixels)):

    if is_pixel_green(pixels[i], 100):
        x = i % width
        x_coordinates.append(x)

# lista que armazena a frequencia de todas as coordenadas x
counter = collections.Counter(x_coordinates)
print('\nA tabela de frequencia das coordenadas dos pixels verdes:\n\n')
print(counter)