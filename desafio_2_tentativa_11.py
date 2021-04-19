from PIL import Image
from utils import is_pixel_green

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import base64

# classe utilizada para descriptografar strings utilizando uma chave (AES)
class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

# chave usada para descriptografar
key = 'Syngenta Digital Hire me'

# abrindo a imagem e convertendo para RGB
image = Image.open('Syngenta.bmp').convert('RGB')

# tamanhos da imagem
width, height = image.size

# objetivo: gerar strings para tentar descriptografar usando a chave fornecida na imagem
pixels = image.getdata()

output_x = ''
output_x_mod_255 = ''
output_y = ''
output_y_mod_255 = ''
output_soma = ''
output_soma_mod_255 = ''
output_sub = ''
output_sub_mod_255 = ''
output_sub_inverse = ''
output_sub_inverse_mod_255 = ''
for i in range(len(pixels)):

    if is_pixel_green(pixels[i], 100):
        x = i % width
        y = i // width

        try:
            output_x += chr(x)
        except:
            output_x += ''
        try:
            output_x_mod_255 += chr(x % 255)
        except:
            output_x_mod_255 += ''
        try:
            output_y += chr(y)
        except:
            output_y += ''
        try:
            output_y_mod_255 += chr(y % 255)
        except:
            output_y_mod_255 += ''
        try:
            output_soma += chr(x + y)
        except:
            output_soma += ''
        try:
            output_soma_mod_255 += chr((x - y) % 255)
        except:
            output_soma_mod_255 += ''
        try:
            output_sub_mod_255 += chr((x - y) % 255)
        except:
            output_sub_mod_255 += ''
        try:
            output_sub_inverse += chr(y-x)
        except:
            output_sub_inverse += ''
        try:
            output_sub_inverse_mod_255 += chr((y-x) % 255)
        except:
            output_sub_inverse_mod_255 += ''

print(f'\nIniciando a descriptografar utilizando a chave "{key}":\n\n')

decryptor = AESCipher(key)

try:
    print('Tentando descriptografar a string gerada a partir das coord x')
    print(decryptor.decrypt(output_x))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir das coord x mod 255')
    print(decryptor.decrypt(output_x_mod_255))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir das coord y')
    print(decryptor.decrypt(output_y))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir das coord y mod 255')
    print(decryptor.decrypt(output_y_mod_255))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir de x+y')
    print(decryptor.decrypt(output_soma))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir de x+y mod 255')
    print(decryptor.decrypt(output_soma_mod_255))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir de x - y')
    print(decryptor.decrypt(output_sub))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir de x - y mod 255')
    print(decryptor.decrypt(output_sub_mod_255))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir de y - x')
    print(decryptor.decrypt(output_sub_inverse))
except:
    print('Nao foi possivel descriptografar\n\n')

try:
    print('Tentando descriptografar a string gerada a partir de y - x mod 255')
    print(decryptor.decrypt(output_sub_inverse_mod_255))
except:
    print('Nao foi possivel descriptografar\n\n')
