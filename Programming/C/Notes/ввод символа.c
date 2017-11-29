#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable : 4996)

int main()
{ 
	system("chcp 1251"); //кодировка русского языка
	system("cls");      //очистка консоли

	
	// Переменная, в которую сохраняется считанный символ
	int rsim = -1;

	//Запрос ввода символа
	printf("Введите символ : \n");

	//Чтение символа из стандартного потока ввода
	rsim = getchar();

	//Вывод результата работы
	printf("Введённый Вами символ : %c\n", rsim);

	system("pause");
	return 0;
}