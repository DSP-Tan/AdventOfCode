#include<stdio.h>
int proc_till_buff( int buff_size);

int main(){
  printf("%d\n",proc_till_buff(4));
  printf("%d\n",proc_till_buff(14));
  }

int proc_till_buff( int buff_size){

  FILE* fp;
  char c, buffer[buff_size];
  int pos,same;


  fp = fopen("input.txt","r");
  for(int i=0; i<buff_size; i++)
    fscanf(fp,"%c",&buffer[i]);


  pos=buff_size;
  while(fscanf(fp,"%c",&c) == 1){
    pos++;

    for(int i=0; i<buff_size-1; i++)
       buffer[i]=buffer[i+1];
    buffer[buff_size-1]=c;

    same=0;
    for(int j=0; j<buff_size; j++)
        for(int k=j+1; k<buff_size; k++)
            if(buffer[j]==buffer[k])
                same=1;
    if( !same )
      break;

    }
  fclose(fp);
  return pos;

  }
