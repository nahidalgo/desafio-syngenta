from PIL import Image
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: imprimir todos os pixels verdes e suas coordenadas
pixels = image.getdata()

green_pixels_count = 0
for i in range(len(pixels)):

    if is_pixel_green(pixels[i], 100):
        x = i % width
        y = i // width

        green_pixels_count += 1

        coord = (x, y)
        coord_sum = x + y
        coord_sub = x - y
        coord_sub_inverse = y - x

        print(f'Green Pixel {green_pixels_count} at pos {coord}\tx+y = {coord_sum}\tx-y = {coord_sub}\ty-x = {coord_sub_inverse}')

# Obs esta analise mais detalhada permite observar que as linhas 0 e 15 da imagem
# nao possuem pixels verdes