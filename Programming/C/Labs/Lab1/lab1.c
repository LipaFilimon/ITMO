#include <stdio.h>
#include <stdlib.h>

int main()
{
	system("chcp 1251"); //êîäèðîâêà ðóññêîãî ÿçûêà
	system("cls");      //î÷èñòêà êîíñîëè


	int a;
	printf("Ââåäèòå öåëîå ÷èñëî:\n");
	scanf("%d", &a);
	printf("Öåëîå ÷èñëî = %d\n\n", a);

	getchar();

	char b;
	printf("Ââåäèòå ñèìâîë:\n");
	scanf("%c", &b);
	printf("Ââåä¸ííûé Âàìè ñèìâîë : %c\n\n", b);



	return 0;
}




