/*
REGRAS:
1> Só um disco pode ser movido de cada vez
2> O disco removido deve ser colocado em outra agulha
3> Um disco maior não pode ser colocado no topo de outro disco menor

Lógica:
 - Mover os n-1 discos de cima da agulha 1 para a agulha 2 usando a
 agulha 3 como agulha intermediária
 - Mover disco número n da agulha 1 pra agulha 3
 - Mover os n-1 discos de cima da agulha 2 pra agulha 3 usando a 
 agulha 1 como agulha intermediária
*/

#include<iostream>

using namespace std;
void move(int,int,int,int);

int main()
{
	int num;
	cout << "Insira o numero de discos: ";
	cin >> num;
	cout << endl;

	move(num,1,3,2);
	system("PAUSE");
	return 0;
}

void move(int count,int a1,int a3,int a2)
{
	if(count > 0)
	{ 
		move(count - 1,a1,a2,a3);
		cout<<"Movendo disco " << count << " de " << a1 << " para " << a3 << "." << endl;
		move(count - 1,a2,a3,a1);

	}

}