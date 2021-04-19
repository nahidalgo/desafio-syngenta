from PIL import Image, ImageDraw
import collections
import base64

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')
image_width, image_height = image.size
print(image_width, image_height)

# definindo um limite para poder dizer se o pixel 
# eh verde ou nao
g_threshold = 100

# contador que guarda o numero de pixels verdes
green_pixels_count = 0

green_pixels_list = [pixel for pixel in image.getdata() if pixel[1] > g_threshold and pixel[1] > pixel[0] and pixel[1] > pixel[2]]

print(len(green_pixels_list))

for pixel in image.getdata():
    r,g,b = pixel

    # se o pixel atender essas condicoes
    # entao ele eh verde
    if g > g_threshold and g > r and g > b:
        green_pixels_count += 1



print(green_pixels_count)


# talvez a mensagem tenha a ver com a posicao dos pixeis verdes

x_coordinates = []
sub_x_y = []
sum_x_y = []
sub_i_x_y = []
pos = 0
chr_list = []
green_pixels_count = 0
x_y_coordinates = []

mapa_coordx_posy = [[] for i in range(image_width)]
for pixel in image.getdata():
    r,g,b = pixel

    # se o pixel atender essas condicoes
    # entao ele eh verde
    if g > g_threshold and g > r and g > b:
        green_pixels_count += 1
        x = pos % 420
        y = pos // 420

        coord = (x, y)
        coord_sum = x + y
        coord_sub = x - y
        coord_sub_inverse = y - x

        mapa_coordx_posy[x].append(y)
        print(f'Green Pixel {green_pixels_count} at pos {coord}\tx+y = {coord_sum}\tx-y = {coord_sub}\ty-x = {coord_sub_inverse}')
        # (96, 192, 0)

        chr_list.append(chr(x))

        x_y_coordinates.append((x,y))
        x_coordinates.append(x)
        sum_x_y.append(coord_sum)
        sub_x_y.append(coord_sub)
        sub_i_x_y.append(coord_sub_inverse)

    elif r < 255 and g < 255 and b < 255 and (r > 0 or g > 0 or b > 0):
        print(pixel)
    
    pos += 1

# eh possivel ver que nao ha repeticao da coordenada y dos pixeis

print()
print()
# Checando se existe ou nao repeticao nas coordenadas x
print(x_coordinates)

# lista que armazena a frequencia de todas as coordenadas x
counter=collections.Counter(x_coordinates)
print(counter)

print()
print()
for numero in x_coordinates:
    print(chr(numero % 255), end='')

for char in chr_list:
    print(char, end='')

def map_value(value, min_from, max_from, min_to, max_to):
    return ((value / (max_from - min_from)) * max_to) - min_to


print()
print()
print()
# Tentando mapear a coordenada x dos pixels de 0 a 420 pra 0 a 255
for numero in x_coordinates:
    numero_normalizado = int(map_value(numero, 0, 419, 0, 255))

    print(chr(numero_normalizado), end='')

# somar todas as coordenadas de x


message = []
aux = 0
m = ''
message = [[0 for col in range(image_height)] for row in range(image_width)]
pos = 0

print()
print()
for pixel in image.getdata():
    r,g,b = pixel
    flag = 0

    x = pos % 420
    y = pos // 420

    # se o pixel atender essas condicoes
    # entao ele eh verde
    if g > g_threshold and g > r and g > b and flag != 1:
        m += '1'
        message[x][y] = '1'
    else:
        m += '0'
        message[x][y] = '0'
    

    if aux == 8:
        aux = 0

        number = int(m, base=2)

        if number != 0:
            print(number, end=',')
        # print(chr(int(m, base=2)), end='')
        m = ''
    
    pos += 1
    aux += 1

# message_str = ''
# bit_counter = 0
# print()
# print()
# for i in range(image_width):
#     for j in range(image_height):
#         message_str += message[i][j]
#         bit_counter += 1

#         if bit_counter == 8:
#             number = int(message_str, base=2)

#             if number != 0:
#                 # print(message_str)
#                 print(chr(number), end='')
            
#             message_str = ''
#             bit_counter = 0


soma_coord_x = 0
for coord in x_coordinates:
    soma_coord_x += coord

print(hex(soma_coord_x))

print()
print()
print()


# Brincando com criptografia e base64 (Sem Sucesso)
# string_normalizado = ''
# string_coordenadas = ''
# string_coordenadas_mod_255 = ''
# for numero in x_coordinates:
#     numero_normalizado = int(map_value(numero, 0, 419, 0, 255))

#     string_coordenadas_mod_255 += chr(numero % 255)
#     string_coordenadas += chr(numero)
#     string_normalizado += chr(numero_normalizado)

# b64_string_normalizado = base64.b64encode(string_normalizado.encode())
# b64_string_coordenadas = base64.b64encode(string_coordenadas.encode())
# b64_string_coordenadas_mod_255 = base64.b64encode(string_coordenadas_mod_255.encode())
# print(string_normalizado)
# print(base64.b64encode(string_normalizado.encode()))
# print(len(base64.b64encode(string_normalizado.encode())))

# print()
# print()
# print(string_coordenadas)
# print(base64.b64encode(string_coordenadas.encode()))
# print(len(base64.b64encode(string_coordenadas.encode())))
# print(len(base64.b64encode(string_coordenadas.encode())))



# soma das coordenadas to ascii

# helper function
def to_utf8(number):
    return chr(int(number))

# output = ''
# for number in sum_x_y:
#     output += to_utf8(number)

# file1 = open("soma_coordenadas_x_y_to_ascii.txt","w")
# file1.write(output)
# file1.close()

# print(output)




# output = ''
# for number in sub_i_x_y:
#     output += to_utf8(number)

# file1 = open("sub_coordenadas_x_y_to_ascii.txt","w")
# file1.write(output)
# file1.close()

# print(output)


syngenta = 'syngenta'

sum_syng = 0
for character in syngenta:
    sum_syng += ord(character)

print(sum_syng)


# Codificando o arquivo inteiro para base64 e tentando uma chave
# with open("Syngenta.bmp", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     print(encoded_string)
#     file1 = open("syngenta_image_base64.txt","w")
#     file1.write(str(encoded_string))
#     file1.close()


# import base64


# Desenhando na imagem e salvando em outro arquivo
with Image.open("Syngenta.bmp") as im:

    for i in range(len(x_y_coordinates) - 1):

        x0, y0 = x_y_coordinates[i]
        x1, y1 = x_y_coordinates[i+1]

        draw = ImageDraw.Draw(im)
        draw.line([x0, y0, x1, y1], fill=128)

        # write to stdout
        im.save('teste.png', "PNG")

# Quais colunas nao possuem pixels verdes?

soma = 0
visited = [0 for x in range(image_width)]
for x_coord in x_coordinates:
    visited[x_coord] = 1
    soma += x_coord

print(f'Soma de todas a coordenadas X = {soma}')

soma = 0
for i in range(len(visited)):
    if visited[i] == 0:
        print(i, end=', ')
        soma += i
print()
print(f'Soma de todas a coordenadas que nao possuem pixles = {soma}')


    


import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

key = 'Syngenta Digital Hire me'

vetor_frequencia = [0 for i in range(image_width)]

pos = 0
for pixel in image.getdata():
    r,g,b = pixel
    x = pos % 420
    y = pos // 420

    if g > g_threshold and g > r and g > b and flag != 1:
        vetor_frequencia[x] += 1
    
    pos += 1
    
print(vetor_frequencia)

vetor_frequencia_sem_0 = [x for x in vetor_frequencia if x != 0]

print(vetor_frequencia_sem_0)


# Desenhando na imagem e salvando em outro arquivo
with Image.open("Syngenta.bmp") as im:

    draw = ImageDraw.Draw(im)
    i = 0
    x = 0
    for coluna in visited:

        while visited[i] == 0:
            i += 1

            if i > image_width - 1:
                break

        for ponto in mapa_coordx_posy[i]:
            print(ponto)
            draw.point((x, ponto), fill=255)
        
        x += 1
        i += 1

        print(f'X = {x} i = {i}')
        


        # write to stdout
        im.save('teste2.png', "PNG")


print(mapa_coordx_posy)