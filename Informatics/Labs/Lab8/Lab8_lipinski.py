import math
from PIL import Image
#import numpy as np
IMAGE_PATH = "./"  # Путь до картинки, с которой будем работать, пустой если находится в той же директоррии, что и программа.
IMAGE_NAME = "pic"  # Имя картинки.
IMAGE_TYPE = "jpg"  # Тип картинки, крайне рекомендуется jpg.

def quantum(pixel):
    r, g, b = pixel
    return round(r / 20) * 20, round(g / 20) * 20, round(b / 20) * 20

def convert(num, to_base=2, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alph[n]
    else:
        return convert(n // to_base, to_base) + alph[n % to_base]

# Task 1

original_image = Image.open(IMAGE_PATH + IMAGE_NAME + "." + IMAGE_TYPE)  # Открываем изображение.
width = original_image.size[0]  # Определяем ширину.
height = original_image.size[1]  # Определяем высоту.
pixels = original_image.load()
channels = 2

# Task 2

for i in range(width):
    for j in range(height):
        pixels[i, j] = quantum(pixels[i, j])    

# Task 3

alphabet = []
prob = []
summa = 0

for i in range(256):
    alphabet.append(0)
    prob.append(0)

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        alphabet[r] += 1

print(alphabet)

for i in range(256):
    summa += alphabet[i]

for i in range(0, 256, 20):
    prob[i] = alphabet[i] / summa
    print(prob[i])     

# Task 4

entropy = 0

for i in range(0, 256, 20):
    if prob[i] != 0:
        entropy -= prob[i] * math.log(prob[i], 2)
print(entropy)     

# Task 5

bin_Code = [[0] * 128 for i in range(128)]

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        binNum = convert(r / 20)
        bin_Code[i][j] = (('0' * (4 - int(len(binNum)))) + binNum)
        print (bin_Code[i][j])

# Task 6
for i in range(0, 256, 20):
   print(alphabet[i])
fano_Code = [[0] * 128 for i in range(128)]

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        if r == 0:                      #A
            fano_Code[i][j] = '1001'
        elif r == 20:                   #B
            fano_Code[i][j] = '010'
        elif r == 40:                   #C
            fano_Code[i][j] = '1000'
        elif r == 60:                   #D
            fano_Code[i][j] = '1100'
        elif r == 80:                   #E
            fano_Code[i][j] = '001'
        elif r == 100:                  #F
            fano_Code[i][j] = '1101'
        elif r == 120:                  #G
            fano_Code[i][j] = '1110'
        elif r == 140:                  #H
            fano_Code[i][j] = '11111'
        elif r == 160:                  #I
            fano_Code[i][j] = '11110'
        elif r == 180:                  #J
            fano_Code[i][j] = '1010'
        elif r == 200:                  #K
            fano_Code[i][j] = '1011'
        elif r == 220:                  #L
            fano_Code[i][j] = '011'
        elif r == 240:                  #M
            fano_Code[i][j] = '000'
print(fano_Code)

# Task 7

haff_Code = [[0] * 128 for i in range(128)]

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        if r == 0:                      #A
            haff_Code[i][j] = '1001'
        elif r == 20:                   #B
            haff_Code[i][j] = '010'
        elif r == 40:                   #C
            haff_Code[i][j] = '1100'
        elif r == 60:                   #D
            haff_Code[i][j] = '0110'
        elif r == 80:                   #E
            haff_Code[i][j] = '100'
        elif r == 100:                  #F
            haff_Code[i][j] = '0011'
        elif r == 120:                  #G
            haff_Code[i][j] = '0010'
        elif r == 140:                  #H
            haff_Code[i][j] = '11010'
        elif r == 160:                  #I
            haff_Code[i][j] = '11011'
        elif r == 180:                  #J
            haff_Code[i][j] = '1010'
        elif r == 200:                  #K
            haff_Code[i][j] = '0111'
        elif r == 220:                  #L
            haff_Code[i][j] = '000'
        elif r == 240:                  #M
            haff_Code[i][j] = '111'
print(haff_Code)

# Task 8

eq_MidLen = 4
fano_MidLen = (2696 * 3 + 2134 * 3 + 1688 * 3 + 1460 * 3 + 1226 * 4 + 1121 * 4 + 1031 * 4 + 980 * 4 + 971 * 4 + 769 * 4 + 748 * 4 + 691 * 5 + 561 * 5) / 16384
haff_MidLen = (2696 * 3 + 2134 * 3 + 1688 * 3 + 1460 * 3 + 1226 * 4 + 1121 * 4 + 1031 * 4 + 980 * 4 + 971 * 4 + 769 * 4 + 748 * 4 + 691 * 5 + 561 * 5) / 16384
print(eq_MidLen)
print(fano_MidLen)
print(haff_MidLen)

# Task 9

original_Size = 4 * 128 * 128
fano_Size = fano_MidLen * 128 * 128
haff_Size = haff_MidLen * 128 * 128
fano_Compress = (original_Size - fano_Size) / original_Size * 100
haff_Compress = (original_Size - haff_Size) / original_Size * 100
print(fano_Compress)
print(haff_Compress)

# Task 10

fano_Eff = 1 - (entropy / fano_MidLen)
haff_Eff = 1 - (entropy / haff_MidLen)
print(fano_Eff)
print(haff_Eff)
