#include<stdio.h>
#include<stdlib.h>

int search(char **lines, int n, char* word,  int x, int y);
int searchX(char **lines, int n );
int buff =12;

int main(){
  FILE *file;
  int i,j,n,N,cnt;
  i=j=n=N=cnt=0;
  int start = buff/2-1;

  file = fopen("input.txt","r"); n=140;
  N=n+buff;

  //char lines[N][N];
  char **lines = (char **)malloc(N * sizeof(char *));
  for (i=0; i<N; i++) lines[i] = (char *)malloc(N * sizeof(char));

  for(i=0;i<N;i++) for(j=0;j<N;j++) lines[i][j]=' ';

  // Read into lines starting after buffer.
  for(i=start;i<n+start;i++)
    fgets(&lines[i][start],N, file);

  for(i=-1;i<=1;i++)
    for(j=-1;j<=1;j++)
      cnt+=search(lines,n,"XMAS",i,j);
  printf("Total Xmas: %d\n",cnt);

  cnt=0;
  cnt = searchX(lines, n);
  printf("Total Xmas: %d\n",cnt);

}

int search(char **lines, int n, char* word,  int x, int y){
  int i,j,k,cnt,yes,nWrd;
  i=j=k=cnt=yes=nWrd=0;
  int start = buff/2-1;

  while( word[nWrd]!='\0') nWrd++;

  for(i=start;i<n+start;i++)
    for(j=start;j<n+start;j++){
      yes=0;
      for(k=0;k<nWrd;k++)
        if(lines[i+k*y][j+k*x]==word[k])
          yes++;
      cnt += (yes==nWrd);
      }
  return cnt;
}

int searchX(char **lines, int n ){
  int i,j,k,cnt;
  int mas1,mas2;
  i=j=k=cnt=0;
  int start = buff/2-1;

  for(i=start;i<n+start;i++)
    for(j=start;j<n+start;j++)
      if(lines[i][j]=='A'){
        mas1=mas2=0;
        mas1=(lines[i-1][j-1]=='M' && lines[i+1][j+1]=='S') || (lines[i-1][j-1]=='S' && lines[i+1][j+1]=='M');
        mas2=(lines[i-1][j+1]=='M' && lines[i+1][j-1]=='S') || (lines[i-1][j+1]=='S' && lines[i+1][j-1]=='M');
        cnt += mas1 && mas2;
        }
  return cnt;
}
