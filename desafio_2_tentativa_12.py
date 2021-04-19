from PIL import Image, ImageDraw
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: ligar todos os pontos visualmente para ver se aparece algum padrao
pixels = image.getdata()

# lista que guarda todas as coordenadas x,y dos pixels verdes
x_y_coordinates = []
green_pixels_count = 0
for i in range(len(pixels)):
    if is_pixel_green(pixels[i], 100):
        x = i % width
        y = i // width

        x_y_coordinates.append((x,y))


# Desenhando na imagem e salvando em outro arquivo comecando de cima para baixo
with Image.open("Syngenta.bmp") as im:

    for i in range(len(x_y_coordinates) - 1):

        x0, y0 = x_y_coordinates[i]
        x1, y1 = x_y_coordinates[i+1]

        draw = ImageDraw.Draw(im)
        draw.line([x0, y0, x1, y1], fill=128)

        # write to stdout
        im.save('ligando_pixels_verdes.png', "PNG")


# ordenando os pixels a partir de x para desenhar da esquerda para direita
def sort_func(coord):
    return coord[0]

x_y_coordinates.sort(key=sort_func)

print(x_y_coordinates)

# Desenhando na imagem e salvando em outro arquivo comecando da esquerda para direita
with Image.open("Syngenta.bmp") as im:

    for i in range(len(x_y_coordinates) - 1):

        x0, y0 = x_y_coordinates[i]
        x1, y1 = x_y_coordinates[i+1]

        draw = ImageDraw.Draw(im)
        draw.line([x0, y0, x1, y1], fill=128)

        # write to stdout
        im.save('ligando_pixels_verdes_dir_esq.png', "PNG")