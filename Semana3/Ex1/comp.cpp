#include <bits/stdc++.h>
#include "comp.h"
using namespace std;


comp::comp(double rc, double ic){
	r = rc;
	i = ic;
	m = sqrt(pow(r,2) + pow(i,2)); 
	a = atan(i/r) * rad2deg;
};

comp op::soma(comp n1, comp n2){
	double r = n1.r + n2.r;
	double i = n1.i + n2.i;
	return comp(r,i); 
};

comp op::subt(comp n1, comp n2){
	double r = n1.r - n2.r;
	double i = n1.i - n2.i;
	return comp(r,i); 
};

comp op::mult(comp n1, comp n2){
	double r = n1.r*n2.r - n1.i*n2.i ;
	double i = n1.r*n2.r + n1.i*n2.i;
	return comp(r,i); 

};

comp op::div(comp n1, comp n2){
	op op;
	
	comp n2conj(n2.r, (-1)*n2.i);
	double num1 = n1.r*n2.r + n1.i*n2.i;
	double num2 = n1.i*n2.r - n1.r*n2.i;
	double d = pow(n2.r,2) + pow(n2.i,2);
	
	return comp(num1/d,num2/d);


};

