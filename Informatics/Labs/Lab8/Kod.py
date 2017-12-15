import sys, array, math
from PIL import Image
#//
file = open("nature.jpg", "rb")
img = Image.open(file)
width = img.size[0]
height = img.size[1]
pixels = img.load()
Pixel_List = []
CountPix = []
Alphabet = []
Number = 0
Number_Of_Positions = width
Symbol_Entropy = 0


	#Преобразование центральной строки
for i in range(width):
    Pixel_List.append(round(pixels[i, height // 2] / 20) * 20)

	#Частота встречи символов, кол-во символов, энтропия
for i in range(round(255 / 20) * 20 + 1):
    count = Pixel_List.count(i)
    CountPix.append(count)
    if CountPix[i] > 0:
        print("Кол-во", i, "=", CountPix[i])
        Number += 1
        Symbol_Entropy += (count / Number_Of_Positions) * math.log2((count / Number_Of_Positions))
        Alphabet.append(i)

print("")
print("Кол-во символов в алфавите:", Number)
print("")
print("Энтропия :", Symbol_Entropy * -1)
print("")

	#Равномерный односимвольный код
print("Равномерный односимвольный код")
print("")
digit = math.ceil(math.log2(Number))
for i in range(Number):
    print("Код", Alphabet[i], "=", bin(i)[2:].zfill(digit))

print("")
	#Коды Фано и Хаффмана
Code_Huffman = ["11", "0110", "10011", "010", "1000", "00", "10010", "0111000", "011111", "011101", "0111101", "0111001", "0111100", "101"]
Code_Fano = ["00", "1000", "1010", "1011", "1001", "110", "11100", "11101", "11110", "111110", "111111", "0100", "0101", "011"]

	#Средняя длина кодовых комбинаций, эффективность, избыточность
Middle_Huff = 0
Middle_Fano = 0
Middle_Bin = 0
for i in range(Number):
    Middle_Huff += len(Code_Huffman[i]) * (CountPix[Alphabet[i]] / Number_Of_Positions)
    Middle_Fano += len(Code_Fano[i]) * (CountPix[Alphabet[i]] / Number_Of_Positions)
    Middle_Bin += digit * (CountPix[Alphabet[i]] / Number_Of_Positions)
print("Средняя длина кодовых комбинаций по Хаффману:", Middle_Huff)
print("")
print("Средняя длина кодовых комбинаций по Фано:", Middle_Fano)
print("")
print("Средняя длина кодовых комбинаций по равномерному односимвольному коду:", Middle_Bin)
print("")
print("Относительная эффективность сжатия кодировкой Фано и односимвольным кодом в", Middle_Bin / Middle_Fano, "раз(а)")
print("")
print("Относительная эффективность сжатия кодировкой Хаффмана и односимвольным кодом в", Middle_Bin / Middle_Huff, "раз(а)")
print("")
print("Относительная избыточность кодировки Хаффмана:", 1 - (Symbol_Entropy * -1) / Middle_Huff)
print("")
print("Относительная избыточность кодировки Фано:", 1 - (Symbol_Entropy * -1) / Middle_Fano)
file.close()
