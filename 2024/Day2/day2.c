#include<stdio.h>
#include<stdlib.h>

int readNum(char *line, int start, int *num);
int countNumbers(char *line);
int checkMonotonic(int *nums, int numcnt, int *bad);
int checkDiffs(    int *nums, int numcnt, int *bad);
int getNewNums(int *nums, int numcnt, int bad, int *NewNums);

int main(){
  FILE *input;
  int i,j, numcnt;
  int bad=0;
  int mono , mono1,  mono2;
  int diffs, diffs1, diffs2;


  //input = fopen("example.txt","r");
  input = fopen("input.txt","r");
  char line[100];

  int safes=0;
  while(fgets(line, 100, input)!=NULL){
    printf("------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------\n");
    numcnt = countNumbers(line);
    int nums[numcnt];
    int NewNums[numcnt-1];

    int next=0;
    i=0;
    do {
      next= readNum(line,next,&nums[i]);
      i++;
      }
    while( next !=0 );

    for(i=0;i<numcnt;i++) printf("%d ",nums[i]);

    printf("\n");
    mono  = checkMonotonic(nums, numcnt, &bad);
    if(!mono){
      printf("%d and %d not monotonic.\n",nums[bad-1],nums[bad]);

      getNewNums(nums, numcnt, bad, NewNums);
      for(i=0;i<numcnt-1;i++) printf("%d ",NewNums[i]);
      printf("\n");
      mono1 = checkMonotonic(NewNums, numcnt-1, &j);
      diffs1 = checkDiffs(NewNums, numcnt-1, &j);

      getNewNums(nums, numcnt, bad-1, NewNums);
      for(i=0;i<numcnt-1;i++) printf("%d ",NewNums[i]);
      printf("\n");
      mono2  = checkMonotonic(NewNums, numcnt-1, &j);
      diffs2 = checkDiffs(NewNums, numcnt-1, &j);

      printf("mono1: %d; mono2: %d newMono %d\n",mono1,mono2, mono1||mono2);
      printf("diff1: %d; diff2: %d newDiff %d\n",diffs1,diffs2, diffs1||diffs2);

      if( (mono1 && diffs1) || (mono2 && diffs2) ){
        safes++;
        printf("safe\n");
        continue;
      }
      continue;

      }

    diffs = checkDiffs(nums,numcnt,&bad);
    if(!diffs){
      printf("%d and %d not diffs.\n",nums[bad-1],nums[bad]);

      getNewNums(nums, numcnt, bad, NewNums);
      for(i=0;i<numcnt-1;i++) printf("%d ",NewNums[i]);
      printf("\n");
      diffs1 = checkDiffs(NewNums, numcnt-1, &j);
      mono1 = checkMonotonic(NewNums, numcnt-1, &j);

      getNewNums(nums, numcnt, bad-1, NewNums);
      for(i=0;i<numcnt-1;i++) printf("%d ",NewNums[i]);
      printf("\n");
      diffs2 = checkDiffs(NewNums, numcnt-1, &j);
      mono2  = checkMonotonic(NewNums, numcnt-1, &j);

      printf("diff1: %d; diff2: %d newDiff %d\n",diffs1,diffs2, diffs1||diffs2);
      printf("mono1: %d; mono2: %d newMono %d\n",mono1,mono2, mono1||mono2);


      if( (mono1 && diffs1) || (mono2 && diffs2) ){
        safes++;
        printf("safe\n");
        continue;
      }
      printf("Unsafe!!!!!!\n");
      continue;


    }


    if(mono && diffs){
      printf("Line good\n");
      safes++;
    }
    else
      printf("line unsafe\n");

    printf("------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------\n");

  }

  printf("There are %d safe things.\n",safes);

  fclose(input);

  return 0;
}

int readNum(char *line, int start, int *num){
  int i=0;
  char c=line[start];
  char number[20];

  for(int j=0;j<20;j++) number[j]='\0';
  while(c!=' ' && c !='\n' && c!='\0'){
    number[i] = c;
    i++;
    c=line[start+i];
  }

  if (i==0){
    return i;
  }
  else {
    sscanf(number,"%d",num);
    return start+i+1;
  }
}


int countNumbers(char *line){
  int cnt=0;
  int i;
  for(i=0; i<100; i++){
    if(line[i]==' ')
      cnt++;
    else if(line[i]=='\n'){
      cnt++;
      break;
    }
  }
  return cnt;
}

int checkMonotonic(int *nums, int numcnt, int *bad){
  int incOrDec = nums[1] > nums[0];
  for(int i=1; i<numcnt; i++)
    if(nums[i] > nums[i-1] != incOrDec){
      *bad = i;
      return 0;
    }
  return 1;
}


int checkDiffs(int *nums, int numcnt, int *bad){
  for(int i=1; i<numcnt; i++){
    int diff = abs(nums[i] - nums[i-1]);
    if(diff <1 || diff > 3){
      *bad = i;
      return 0;
      }
    }
  return 1;
}

int getNewNums(int *nums, int numcnt, int bad, int *NewNums){
  int j=0;
  for(int i=0;i<numcnt;i++){
    if(i==bad)
      continue;
    NewNums[j] = nums[i];
    j++;
    }
  return 0;
  }
