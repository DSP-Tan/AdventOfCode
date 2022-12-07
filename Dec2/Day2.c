#include <stdio.h>
#include <stdlib.h>
int main(){

FILE *fp;

int i;
char A,B,C,D;
char line[100];

fp = fopen("input.txt", "r");
//fgets(line, 80, fp);
//printf("%d\n",i);
//printf("%c %c", line[0], line[2]);

//fscanf(fp,"%c %c", &A,&B);
//printf("%c %c", A, B);

//while( fgets(line, 80, fp) != NULL ){
//  sscanf(line,'%d %d', &A, &B);
//  printf("%d %d",A, B);
//  }

i=0;
while( fscanf(fp, "%c%c%c%c", &A,&C, &B,&C) == 4 ){
  printf("%c %c\n",A, B);
  i++;
  }
printf("%d\n",i);
//while ( read= getline(&line, &len, fp) != -1 ) if (isspace(line[0])) n_elves++;
//fclose(fp);

}
