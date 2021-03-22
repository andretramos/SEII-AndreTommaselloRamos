#include<stdio.h>
#include<stdlib.h>
#include<string.h>


//Main
int main(){
	//Declaração de variáveis
  size_t tamanho_buffer =1024; // Representa leitura de 1Mb
  size_t byteslidos;
  char *buffer;
  FILE *f_in,*f_out;

  if (!(f_in = fopen("teste.txt","rb"))){
    fprintf(stderr,"O arquivo %s não foi encontrado\n","teste.txt");
    return -1;
  }if (!(f_out = fopen("teste_copia.txt","wb"))){
    fprintf(stderr,"O arquivo %s não pode ser criado\n","teste_copia.txt");
    return -1;
  }
  buffer =(char*) malloc(tamanho_buffer);
  if(!buffer){
     fprintf(stderr,"Não foi possivel alocar memoria\n");
     goto freeFiles;
  }

  while(!feof(f_in)){
    byteslidos = fread(buffer,1,tamanho_buffer,f_in);
    printf("%d\n",byteslidos);
    if(byteslidos <=0)break;
    fwrite(buffer,byteslidos,1,f_out);
  }
  free(buffer);
  freeFiles:
  fclose(f_in);
  fclose(f_out);
  
  return 0;
}
