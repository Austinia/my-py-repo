#include <stdio.h>

int main()
{
	printf("Hello World!\n");
	//���� �ּ�
	/*
	���� �̻� �ּ�
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
	/*
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
	*/
	printf("sizeof char : %d\n", sizeof(char));
	printf("sizeof int : %d\n", sizeof(int));
	printf("sizeof float : %d\n", sizeof(float));
	printf("sizeof double : %d\n", sizeof(double));
	const int num1 = 100;
	printf("num1 = %d\n", num1);
	//num1 = 200;

	int n1, n2, n3;
	n1 = 1;
	n2 = 1;
	n3 = n1++ + ++n2;
	printf("n1 = %d, n2 = %d, n3 = %d\n", n1, n2, n3);
	printf("5 > 3 = %d\n", 5 > 3);
	printf("5 >= 3 = %d\n", 5 >= 3);
	printf("5 < 3 = %d\n", 5 < 3);
	printf("5 <= 3 = %d\n", 5 <= 3);
	printf("5 == 3 = %d\n", 5 == 3);
	printf("5 != 3 = %d\n", 5 != 3);

	int yes = 1, no = 0;
	printf("yes && no = %d\n", yes && no);
	printf("yes || no = %d\n", yes || no);
	printf("!yes = %d, !no = %d\n", !yes, !no);

	printf("%d\n", 10 / 3);
	printf("%0.2f\n", (float)10 / 3);

	/*char infor;
	printf(" ���� ? (M or F)");
	scanf_s("%c", &infor);
	printf("���� : %s \n", (infor == 'M' ? "��" : "��"));
	*/

	/*int num;
	scanf_s("%d", &num);
	if (num > 0)
		printf("�ڿ���\n");
	if (num % 2 == 0)
		printf("¦��\n");
	else
		printf("Ȧ��\n");
		*/

	/*int age;
	printf("���̸� �Է� :");
	scanf_s("%d", &age);
	if (age > 18)
		printf("�\n");
	else if (age > 12)
		printf("û�ҳ�\n");
	else if (age > 1)
		printf("���\n");
	else
		printf("�Է¿���\n");
		*/

	int score;
	printf("�л��� ���� :");
	scanf_s("%d", &score);
	if (score > 100)
		goto error;
	if (score < 0)
		goto error;
	switch (score/10)
	{
	case 10:
	case 9:
		printf("A ����\n");
		break;
	case 8:
		printf("B ����\n");
		break;
	case 7:
		printf("C ����\n");
		break;
	case 6:
		printf("D ����\n");
		break;
	default:
		printf("F ����\n");
		break;
	}
	return 0;
	error:
	printf("���� ��ȿ���� ����\n");
	return 1;
}