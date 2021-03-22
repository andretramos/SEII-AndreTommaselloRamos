#include <bits/stdc++.h>
#include "comp.h"

#define PI 3.141592
#define rad2deg (180/PI)
#define deg2rad (PI/180)

using namespace std;

int main(){
	cout << "Início do programa: " << endl;
	op op;

	comp n1(5,-3);
	comp n2(2,3);

	comp soma = op.soma(n1,n2);
	comp subt = op.subt(n1,n2);
	comp mult = op.mult(n1,n2);
	comp div = op.div(n1,n2);

	cout << "n1: " << n1.r << " " << n1.i << "i" << endl << "Mod: " << n1.m << "Arg: " << n1.a << endl;
	cout << "n2: " << n2.r << " " << n2.i << "i" << endl << "Mod: " << n2.m << "Arg: " << n2.a << endl;
	cout << "n1+n2: " << soma.r << " " << soma.i << "i"<< endl;
	cout << "n1-n2: " << subt.r << " " << subt.i << "i"<< endl;
	cout << "n1*n2: " << mult.r << " " << mult.i << "i"<< endl;
	cout << "n1/n2: " << div.r << " " << div.i << "i"<< endl;

}
