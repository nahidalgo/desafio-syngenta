from PIL import Image

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')


# definindo um threshold para definir o nivel de verde
# este passo é opcional mas seria útil caso a imagem tivesse
# diferentes cores de pixels
g_threshold = 100

# primeira solucao utilizando compreensao de lista (paradigma funcional)
# as condições aplicadas são:
# - o valor do canal verde deve ser maior que o threshold
# - o valor do canal verde deve ser maior que o canal vermelho e azul
green_pixels_count = len([pixel for pixel in image.getdata() if pixel[1] > g_threshold and pixel[1] > pixel[0] and pixel[1] > pixel[2]])

print(f'Total de pixels verdes utilizando compreensao de lista: {green_pixels_count} pixels')


# segunda solução utilizando um loop for (paradigma imperativo)

# resetando o contador para 0
green_pixels_count = 0

# percorre todos os pixels da imagem
for pixel in image.getdata():
    # fazendo o unpacking da tupla contendo os valores de R, G e B do pixel
    r,g,b = pixel

    # as mesmas condições que na primeira solução
    if g > g_threshold and g > r and g > b:
        green_pixels_count += 1

print(f'Total de pixels verdes utilizando o loop for: {green_pixels_count} pixels')
