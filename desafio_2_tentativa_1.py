from PIL import Image, ImageEnhance

# abrindo a imagem e convertendo para RGB
image = Image.open("Syngenta.bmp").convert('RGB')

# objeto da classe Brightness que permite alterar o brilho da imagem
enhancer = ImageEnhance.Brightness(image)

# fator de aumento de brilho
factor = 5
image_output = enhancer.enhance(factor)
image_output.save('syngenta_brilho_maior.png')