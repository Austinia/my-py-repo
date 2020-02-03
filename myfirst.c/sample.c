#include <stdio.h>

int main()
{
	printf("Hello World!\n");
	//한줄 주석
	/*
	두줄 이상 주석
	*/
	int a;
	int b;
	a = 10;
	b = 5;
	printf("a = %d, b = %d\n", a, b);
	printf("%d,\t%x\n", 16, 16);
	printf("%f,\t%g\n", 3.01, 1000000.3412567);
	printf("%-15c\n", 'C');
	printf("%+15s\n", "Language");

	int number;
	char letter;
	float realnumber;

	printf("number? ");
	scanf_s("%d", &number);
	scanf_s("%*c");
	printf("realnumber? ");
	scanf_s("%f", &realnumber);
	scanf_s("%*c");
	printf("letter? ");
	scanf_s("%c", &letter);
	printf("number = %d, realnumber = %0.2f, letter = %c\n", number, realnumber, letter);
}