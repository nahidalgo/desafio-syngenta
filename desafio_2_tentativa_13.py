from PIL import Image, ImageDraw
from utils import is_pixel_green

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: retirar todas as colunas do desenho que nao possuem pixel e redesenhar os pixels
# restantes
pixels = image.getdata()

# lista de listas que contem todos os pixels em uma determinada coluna
mapa_coordx_posy = [[] for i in range(width)]
for i in range(len(pixels)):
    if is_pixel_green(pixels[i], 100):
        x = i % width
        y = i // width
        
        mapa_coordx_posy[x].append(y)


with Image.open("Syngenta.bmp") as im:

    draw = ImageDraw.Draw(im)

    # indice que mapeia a coluna original para a nova coluna sem os espacos
    mapped_x = 0
    for coluna in range(len(mapa_coordx_posy)):

        if len(mapa_coordx_posy[coluna]) == 0:
            continue

        for ponto in mapa_coordx_posy[coluna]:
            draw.point((mapped_x, ponto), fill=255)

        mapped_x += 1
        
    im.save('pixels_sem_espacamento.png', "PNG")