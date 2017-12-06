import sys, random, copy
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

IMAGE_PATH = "" #Путь до картинки, с которой будем работать, пустой если находится в той же директоррии, что и программа.
IMAGE_NAME = "Pic" #Имя картинки.
IMAGE_TYPE = "jpg" #Тип картинки, крайне рекомендуется jpg.

original_image = Image.open(IMAGE_PATH + IMAGE_NAME + "." + IMAGE_TYPE) #Открываем изображение. 
#draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
image = Image.open("Pic.jpg")
draw = ImageDraw.Draw(image)
#ЛИНЕЙНЫЕ ФИЛЬТРЫ

#Константное преобразование
def constant(pixel):
    r, g, b = pixel
    return r, g, b

#Выделение красной компоненты.
def only_red(pixel):
    r, g, b = pixel
    return r, 0, 0
#Выделение зеленой компоненты.
def only_green(pixel):
    r, g, b = pixel
    return 0, g, 0         
#Выделение синей компоненты:
def only_blue(pixel):
    r, g, b = pixel
    return 0, 0, b
#Оттенки серого:
def grey(pixel):
    r, g, b = pixel
    S = (r + g + b) // 3
    return S, S, S
#Сепия
def Sepia(pixel):
    r, g, b = pixel
    S = (r + g + b) // 3
    r = S + 30 * 2
    g = S + 30
    b = S
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    return r, g, b
#Сепия с голубым оттенком
def Sepia_blue(pixel):
    k = 20
    r, g, b = pixel
    S = (r + g + b) / 3
    r, g, b = S + 2 * k, S + k, S              #ДОДЕЛАТЬ СТИЛИСТИКУ
    return int(r), int(g), int(b) + 150   
#Негатив
def Negative(pixel):
    r, g, b = pixel
    return 255-r, 255-g, 255-b
#Шумы
def Noises(pixel):
    r, g, b = pixel
    rand = random.randint(-70, 70)
    r+=rand
    g+=rand
    b+=rand
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    return  r, g, b
#Повышенная яркость
def Bright(pixel):
    r, g, b = pixel
    r+=150
    g+=150
    b+=150
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    return r, g, b
#Пониженная яркость
def Dark(pixel):
    r, g, b = pixel
    r-=150
    g-=150
    b-=150
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    return r, g, b
#Черный или белый
def BlackOrWhite(pixel):
    r, g, b = pixel
    S=r+g+b
    if (S > (((255 + 100) // 2) * 3)):
        r, g, b = 255, 255, 255
    else:
        r, g, b = 0, 0, 0
    return r, g, b
#Свой фильтр
def MyFilter(pixel):
    r, g, b = pixel
    return ((g + b + r) // 3) + (2 * 50) + 50, ((r + b + g) // 3) + 50, ((b + g + r) // 3) + 70 
    #((g + b + r) // 3) + (2 * 30) + 30, ((r + b + g) // 3) + 30, ((b + g + r) // 3) + 60

#Выделение красной компоненты.
#Список преобразований
linear_transformations = [constant, only_red]

#Последовательное применение всех преобразований с сохранением результата.
for transformation in linear_transformations:
    image = original_image.copy() #Создаем новое изображение, чтобы не испортить оригинальное.
    width = image.size[0] #Определяем ширину. 
    height = image.size[1] #Определяем высоту.  
    pixels = image.load() #Выгружаем значения пикселей.
    
    #Перебираем каждый пиксель
    for i in range(width):
        for j in range(height):
            pixels[i, j] = transformation(pixels[i, j]) #Применяем текущее преобразование.
    
    image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE); #Сохранение картинки.

#Выделение зеленой компоненты.
linear_transformations2 = [constant, only_green]

for transformation in linear_transformations2:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Выделение синей компоненты.
linear_transformations3 = [constant, only_blue]

for transformation in linear_transformations3:
            image = original_image.copy()
            width = image.size[0]
            height = image.size[1]
            pixels = image.load()


            for i in range(width):
                for j in range(height):
                    pixels[i, j] = transformation(pixels[i, j])

            image.save(
                IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Оттенки серого
linear_transformations4 = [constant, grey]

for transformation in linear_transformations4:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Сепия
linear_transformations5 = [constant, Sepia]

for transformation in linear_transformations5:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Сепия с голубым оттенком
linear_transformations5 = [constant, Sepia_blue]

for transformation in linear_transformations5:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Негатив
linear_transformations6 = [constant, Negative]

for transformation in linear_transformations6:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Добавление шумов
linear_transformations7 = [constant, Noises]

for transformation in linear_transformations7:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Увеличение яркости
linear_transformations8 = [constant, Bright]

for transformation in linear_transformations8:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Уменьшение яркости
linear_transformations9 = [constant, Dark]

for transformation in linear_transformations9:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

#Черный или белый
linear_transformations10 = [constant, BlackOrWhite]

for transformation in linear_transformations10:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);

linear_transformations11 = [constant, MyFilter]

for transformation in linear_transformations11:
        image = original_image.copy()
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()


        for i in range(width):
            for j in range(height):
                pixels[i, j] = transformation(pixels[i, j])

        image.save(IMAGE_PATH + IMAGE_NAME + "_" + transformation.__name__ + "." + IMAGE_TYPE);
#МАТРИЧНЫЕ ФИЛЬТРЫ

#Константная матрица 3x3.
def const(): 
    return [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

matrix_filters = [const]

def matrix_transformation(old_pixels, width, height, x, y, get_matrix):
    matrix = get_matrix()
    n = len(matrix) #Узнаем размерность матрицы.
    new_color = [0, 0, 0]
    matrix_sum = 0 #Посчитаем сумму в матрице преобразования для того, чтобы потом поделить на это значение.
                   #Таким образом интенсивность изображения не измениться.
    #Перебираем соседей
    for i in range(n):
        for j in range(n):
            new_x = x - n // 2 + i  #Вычисляем координату соседа, с учетом того, что "мы" в центре матрицы.
            new_y = y - n // 2 + j
           
            #Проверяем соседа на существование.
            if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
                matrix_sum += matrix[i][j]
                #Перебираем цветовую компоненту.
                for c in range(3):
                    new_color[c] += old_pixels[new_x, new_y][c] * matrix[i][j] #Добавляем цвет соседа умноженный на коэффициент из матрицы.
    
    for c in range(3):
        if matrix_sum != 0:
            new_color[c] /= matrix_sum #Нормируем цвет.
        else:
            new_color[c] = 0
    return int(new_color[0]), int(new_color[1]), int(new_color[2])

for matrix in matrix_filters:
    image = original_image.copy() #Создаем новое изображение, чтобы не испортить оригинальное.
    width = image.size[0] #Определяем ширину.
    height = image.size[1] #Определяем высоту.
    pixels = image.load() #Выгружаем значения пикселей.
    old_pixels = original_image.load() #Выгружаем значения пикселей оригинального изображения.
    
    #Перебираем каждый пиксель
    for i in range(width):
        for j in range(height):
            pixels[i, j] = matrix_transformation(old_pixels, width, height, i, j, matrix) #Применяем текущее преобразование.

#Фильтр улучшения чёткости
def const2():
    return [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]


matrix_filters2 = [const2]


def matrix_transformation2(old_pixels, width, height, x, y, get_matrix2):
    matrix2 = get_matrix2()
    n = len(matrix2)  # Узнаем размерность матрицы.
    new_color = [0, 0, 0]
    matrix_sum2 = 0  # Посчитаем сумму в матрице преобразования для того, чтобы потом поделить на это значение.
    # Таким образом интенсивность изображения не измениться.
    # Перебираем соседей
    for i in range(n):
        for j in range(n):
            new_x = x - n // 2 + i  # Вычисляем координату соседа, с учетом того, что "мы" в центре матрицы.
            new_y = y - n // 2 + j

            # Проверяем соседа на существование.
            if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
                matrix_sum2 += matrix2[i][j]
                # Перебираем цветовую компоненту.
                for c in range(3):
                    new_color[c] += old_pixels[new_x, new_y][c] * matrix2[i][
                        j]  # Добавляем цвет соседа умноженный на коэффициент из матрицы.

    for c in range(3):
        if matrix_sum2 != 0:
            new_color[c] /= matrix_sum2  # Нормируем цвет.
        else:
            new_color[c] = 0
    return int(new_color[0]), int(new_color[1]), int(new_color[2])


for matrix2 in matrix_filters2:
    image = original_image.copy()  # Создаем новое изображение, чтобы не испортить оригинальное.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pixels = image.load()  # Выгружаем значения пикселей.
    old_pixels = original_image.load()  # Выгружаем значения пикселей оригинального изображения.

    # Перебираем каждый пиксель
    for i in range(width):
        for j in range(height):
            pixels[i, j] = matrix_transformation2(old_pixels, width, height, i, j,
                                                 matrix2)  # Применяем текущее преобразование.

    image.save(IMAGE_PATH + IMAGE_NAME + "_Sharp" + "." + IMAGE_TYPE);  # Сохранение картинки.

#Фильтр размытия
def const3():
    return [[0.000789, 0.006581, 0.013347, 0.006581, 0.000789], [0.006581, 0.054901, 0.111345, 0.054901, 0.006581],
            [0.013347, 0.111345, 0.225821, 0.111345, 0.013347 ],[0.006581, 0.054901, 0.111345, 0.054901,0.006581],
            [0.000789, 0.006581, 0.013347, 0.006581, 0.000789]]


matrix_filters3 = [const3]


def matrix_transformation3(old_pixels, width, height, x, y, get_matrix3):
    matrix3 = get_matrix3()
    n = len(matrix3)  # Узнаем размерность матрицы.
    new_color = [0, 0, 0]
    matrix_sum3 = 0  # Посчитаем сумму в матрице преобразования для того, чтобы потом поделить на это значение.
    # Таким образом интенсивность изображения не измениться.
    # Перебираем соседей
    for i in range(n):
        for j in range(n):
            new_x = x - n // 2 + i  # Вычисляем координату соседа, с учетом того, что "мы" в центре матрицы.
            new_y = y - n // 2 + j

            # Проверяем соседа на существование.
            if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
                matrix_sum3 += matrix3[i][j]
                # Перебираем цветовую компоненту.
                for c in range(3):
                    new_color[c] += old_pixels[new_x, new_y][c] * matrix3[i][
                        j]  # Добавляем цвет соседа умноженный на коэффициент из матрицы.

    for c in range(3):
        if matrix_sum3 != 0:
            new_color[c] /= matrix_sum3  # Нормируем цвет.
        else:
            new_color[c] = 0
    return int(new_color[0]), int(new_color[1]), int(new_color[2])


for matrix3 in matrix_filters3:
    image = original_image.copy()  # Создаем новое изображение, чтобы не испортить оригинальное.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pixels = image.load()  # Выгружаем значения пикселей.
    old_pixels = original_image.load()  # Выгружаем значения пикселей оригинального изображения.

    # Перебираем каждый пиксель
    for i in range(width):
        for j in range(height):
            pixels[i, j] = matrix_transformation3(old_pixels, width, height, i, j,
                                                 matrix3)  # Применяем текущее преобразование.

    image.save(IMAGE_PATH + IMAGE_NAME + "_Blur" + "." + IMAGE_TYPE);  # Сохранение картинки.


def const4():
    return [[1,0 ,0 ,0 ,1], [0 ,0 ,0 ,0 ,0],[0 ,0 ,0 ,0 ,0],[0 ,0 ,0 ,0 ,0],[1,0 ,0 ,0 ,1]]


IMAGE_ROUTE = "" #Путь до картинки, с которой будем работать, пустой если находится в той же директоррии, что и программа.
IMAGE_NAMAE = "mypic" #Имя картинки.
IMAGE_CLASS = "jpg" #Тип картинки, крайне рекомендуется jpg.

original_image2 = Image.open(IMAGE_ROUTE + IMAGE_NAMAE + "." + IMAGE_CLASS) #Открываем изображение.


matrix_filters4 = [const4]


def matrix_transformation4(old_pixels, width, height, x, y, get_matrix4):
    matrix4 = get_matrix4()
    n = len(matrix4)  # Узнаем размерность матрицы.
    new_color = [0, 0, 0]
    matrix_sum4 = 0  # Посчитаем сумму в матрице преобразования для того, чтобы потом поделить на это значение.
    # Таким образом интенсивность изображения не измениться.
    # Перебираем соседей
    for i in range(n):
        for j in range(n):
            new_x = x - n // 2 + i  # Вычисляем координату соседа, с учетом того, что "мы" в центре матрицы.
            new_y = y - n // 2 + j

            # Проверяем соседа на существование.
            if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
                matrix_sum4 += matrix4[i][j]
                # Перебираем цветовую компоненту.
                for c in range(3):
                    new_color[c] += old_pixels[new_x, new_y][c] * matrix4[i][
                        j]  # Добавляем цвет соседа умноженный на коэффициент из матрицы.

    for c in range(3):
        if matrix_sum4 != 0:
            new_color[c] /= matrix_sum4  # Нормируем цвет.
        else:
            new_color[c] = 0
    return int(new_color[0]), int(new_color[1]), int(new_color[2])


for matrix4 in matrix_filters4:
    image = original_image2.copy()  # Создаем новое изображение, чтобы не испортить оригинальное.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pixels = image.load()  # Выгружаем значения пикселей.
    old_pixels = original_image2.load()  # Выгружаем значения пикселей оригинального изображения.
    # Перебираем каждый пиксель
    for i in range(width):
        for j in range(height):
            pixels[i, j] = matrix_transformation4(old_pixels, width, height, i, j,
                                                 matrix4)  # Применяем текущее преобразование.

    image.save(IMAGE_PATH + IMAGE_NAME + "_my" + "." + IMAGE_TYPE);  # Сохранение картинки. 







