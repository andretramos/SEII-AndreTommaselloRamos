#include <bits/stdc++.h> // Incluindo bibliotecas padrão

#define PI 3.141592
#define rad2deg (180/PI)
#define deg2rad (PI/180)

using namespace std;

class comp{


//Definição dos elementos matemáticos
public:
	double r;  	// Parte real
	double i;		// Parte imaginária
	double m;		// Módulo
	double a;		// Argumento
	//Definição do construtor
	comp(double rc, double ic);

};

class op {
public:
	comp soma(comp n1, comp n2);
	comp subt(comp n1, comp n2);
	comp mult(comp n1, comp n2);
	comp div(comp n1, comp n2);

};