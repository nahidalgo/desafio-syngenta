from PIL import Image

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# o objetivo desta tentativa é checar se existe alguma cor
# de pixel diferente ou leves variações nas cores podendo
# indicar algum tipo de esteganografia

# lista de tuplas (R, G, B) que armazena as cores da imagem
pixel_colors = []

for pixel in image.getdata():
    # se nao tivermos a cor do pixel na lista
    # entao adicione-o

    # O(n) -> complexidade total O(n * pixels) - cuidado
    if not pixel in pixel_colors:
        pixel_colors.append(pixel)

num_colors = len(pixel_colors)

print(f'A imagem possui {num_colors} cores diferentes sendo elas:')

for color in pixel_colors:
    print(color)
    
