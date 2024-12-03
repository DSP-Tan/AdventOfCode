#include<string.h>
#include<stdio.h>
#include<stdlib.h>

int findWord(char *line, int nLine, int start, char *word, int nWord);
int getNumber(char *line, int nLine, int start, int *multo );
int doOrDont(char *line, int cnt, int location);

int main() {
  int i,j,sum,cnt,yes;
  int ni1, ni2, iMul, mulCnt;
  int n1, n2;
  FILE *file;
  sum=0;

  char *mul= "mul(";

  // Open file and count legth of first line
  file = fopen("input.txt","r");
  cnt=0; while(fgetc(file)!=EOF) cnt++; rewind(file);

  //char line[cnt];
  cnt=18182;
  char line[cnt];
  //-----------------------------------------------------------
  //-----------------------------------------------------------
  // To get all the mults in the line we do: findWord, then findNum twice.
  // If findWord gives -1, the loop ends, if findNum either way doesn't work,
  // we go to next find word.
  for(j=0;j<cnt;j++) line[j]='\0';
  fgets(line, cnt, file);
  //char *dont = "don't()";
  //char *dot = "do()";
  //int di=0;
  //int doOrDont=1;
  //while(di !=-1){
  //  if(doOrDont){
  //    di=findWord(line, cnt, di, dont, 7);
  //    printf("Don't: %d\n",di);
  //    doOrDont=0;
  //  }
  //  else{
  //    di=findWord(line, cnt, di, dot, 4);
  //    printf("Do: %d\n",di);
  //    doOrDont=1;
  //    }

  //  }

  //for(i=0; i<6; i++){

  //for(j=0;j<cnt;j++) line[j]='\0';
  //fgets(line, 4000, file);
  printf("%s\n",line);
  //cnt = 4000;
  iMul=0;
  iMul=findWord(line, cnt, iMul, mul, 4);
  while(iMul !=-1){
    mulCnt +=  (iMul != -1) ? 1 : 0;

    printf("mul %d ends at %d\n",mulCnt, iMul);
    ni1 = getNumber(line, cnt, iMul,&n1 );
    ni2 = getNumber(line, cnt, ni1, &n2 );

    if(ni1 && ni2){
      printf("Number1: %d\n",n1);
      printf("Number2: %d\n",n2);
      if(doOrDont(line,cnt,ni1))
        sum +=n1*n2;
      }
    else
      printf("Bad Mul.\n");

    iMul=findWord(line, cnt, iMul, mul, 4);
    }

  //  /*Now check for <number> - <,> - <number> <)>*/

  printf("sum: %d\n",sum);
  //}
  return sum;


}

int findWord(char *line, int nLine, int start, char *word, int nWord){
  // line is the line we are searching; nLine is its size.
  // start is where we start searching from.
  // word is the word we are searching for, and nWord is its size.
  int i,yes=0;
  for(i=start; i<nLine; i++){
    if(line[i]==word[yes]){
      yes++;
      if(yes == nWord)
        return i;
      }
    else
      yes = 0;
    }
  return -1;
}


int getNumber(char *line, int nLine, int start, int *multo ){
  // start refers to the index of the first letter before number:  ( or ,
  int i,j;
  char chrStr[5];
  for(i=0;i<5;i++) chrStr[i]='\0';

  j=0;
  for(i=start+1; i<start+4; i++){  // starts at index preceeding number
    //printf("%c\n",line[i]);
    if( !(line[i]>=48 && line[i] <=57) )
      return 0;
    else{
      chrStr[j]=line[i];
      j++;
      }
    if( (line[i+1]==',' || line[i+1] ==')') ){
      sscanf(chrStr,"%d",multo);
      return i+1; //return index of comma
      }
    }
  return 0;
  }

int doOrDont(char *line, int cnt, int location){
  int lastDo, lastDont,i;
  char *dont = "don't()";
  char *dot = "do()";

  lastDo = lastDont = 0;

  if(location < findWord(line,cnt,0,dont, 7))
    return 1;

  i=0;
  while( lastDo < location && lastDo !=-1){
    i= lastDo;
    lastDo = findWord(line,cnt,i,dot,4);
    }
  lastDo = i;
  i=0;
  while( lastDont < location && lastDont !=-1){
    i= lastDont;
    lastDont = findWord(line,cnt,i,dont,7);
    }
  lastDont = i;
  printf("The nearest do to this point is %d, the nearest don't is %d\n",lastDo,lastDont);
  printf("This is a %d\n",lastDo>lastDont);

  return (lastDo > lastDont);

}
