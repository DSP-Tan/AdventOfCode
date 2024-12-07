#include<stdio.h>
#include<stdlib.h>

int mapDir(int dir, int *di, int *dj);
int getPositionDir(char **lines,  int n, int* pos);
int moveGuard(char** lines, int n, int dir, int* pos);
int dirSymbol(int dir);
void printMap(char **lines,int n);
void resetMap(char **lines, char **lines0, int n);
int walk(char **lines, int n, int *pos, int print);


int main(){
  FILE *file;
  int i,j,k,n,dir,cnt,Xcnt,revisit, pos[2],pos0[2];
  char c;
  i=j=k=n=revisit=cnt=Xcnt=dir=0;

  file = fopen("input.txt","r"); n=130;

  char **lines = (char **)malloc(n * sizeof(char *));
  for (i=0; i<n; i++) lines[i] = (char *)malloc(n * sizeof(char));
  for (i=0; i<n; i++) for(j=0;j<n;j++) lines[i][j]=' ';

  for(i=0;i<n;i++)
    for(j=0;j<n+1;j++){
      c = fgetc(file) ;
      if(c=='\n') continue;
      else        lines[i][j]=c;
      }
  //printf("Original Map:");
  //printMap(lines, n);

  char **lines0 = (char **)malloc(n * sizeof(char *));
  for (i=0; i<n; i++) lines0[i] = (char *)malloc(n * sizeof(char));
  for (i=0; i<n; i++) for(j=0;j<n;j++) lines0[i][j]=lines[i][j];

  /*--------------------------------------------------------------------------*/
  /*--------------------------------------------------------------------------*/
  // First Walk
  printf("First walk:\n");
  cnt=0;
  dir = getPositionDir(lines, n,  pos);
  pos0[0]=pos[0]; pos0[1]=pos[1];

  cnt += walk(lines, n, pos,0);
  //printMap(lines, n);

  // Record Steps
  for(i=0;i<n;i++) for(j=0;j<n;j++) if(lines[i][j]=='X') Xcnt++;
  printf("%d distinct positinos visited\n",Xcnt);
  int Xs[Xcnt][2]; k=0;
  for(i=0;i<n;i++) for(j=0;j<n;j++) if(lines[i][j]=='X'){
    Xs[k][0]=i; Xs[k][1]=j;
    k++;
    }

  // Place Obstacles
  cnt=0;
  int x1, y1;
  for(i=0;i<Xcnt;i++){
    x1= Xs[i][0];
    y1= Xs[i][1];

    if(x1==pos0[0] && y1 == pos0[1])
      continue;
    resetMap(lines,lines0,n);
    dir = getPositionDir(lines, n,  pos);
    lines[x1][y1]='!';

    cnt += walk(lines, n, pos,0);
    }
  printf("Infinites: %d",cnt);

  return cnt;

}

int mapDir(int dir, int *di, int *dj){
  switch(dir){
    case 1: {*di=-1; *dj=0;  return 1; }
    case 2: {*di=0;  *dj=1;  return 1; }
    case 3: {*di=1;  *dj=0;  return 1; }
    case 4: {*di=0;  *dj=-1; return 1; }
  }
  printf("Invalid dir provided\n");
  return 0;
}


int dirSymbol(int dir){
  switch(dir){
    case 1: { return '^'; }
    case 2: { return '>'; }
    case 3: { return 'v'; }
    case 4: { return '<'; }
  }
  return -1;
}


// Directions will be 1 (up), 2 (right), 3 (down ), 4 (left)
// Turning cylces 1=>2=>3=>4=>1
int moveGuard(char** lines, int n, int dir, int* pos){
  int di, dj,i,j, blocked,out;
  i=pos[0]; j=pos[1];

  lines[i][j] = 'X';

  mapDir(dir, &di, &dj);
  out = (i+di ==n) || (j+dj==n) || (i+di ==-1) || (j+dj==-1);
  if(out)
    return -1;


  blocked = lines[i+di][j+dj] =='#' || lines[i+di][j+dj]== '!';
  while(blocked){
    dir = dir==4 ? 1 : dir+1;
    mapDir(dir, &di,&dj);
    blocked = lines[i+di][j+dj] =='#' || lines[i+di][j+dj]== '!';
    }

  pos[0]+=di;
  pos[1]+=dj;
  lines[pos[0]][pos[1]] = dirSymbol(dir);
  return dir;
}


int getPositionDir(char **lines, int n, int* pos){
  // Read the position of the guard into pos, and return its direction
  int i, j;
  for(i=0;i<n;i++)
    for(j=0;j<n;j++){
      if(lines[i][j]>'.'){
        pos[0]=i; pos[1]=j;
        switch (lines[i][j]){
          case '^': return 1;
          case '>': return 2;
          case 'v': return 3;
          case '<': return 4;
          }
        }
      }
  return -1;
}

void printMap(char **lines,int n){
  printf("\n\n");
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++)
      printf("%c",lines[i][j]);
    printf("\n");
    }
}

void resetMap(char **lines, char **lines0, int n){
  for(int i=0; i<n; i++)
    for(int j=0; j<n; j++)
      lines[i][j] = lines0[i][j];
}

int walk(char **lines, int n, int *pos, int print){
  int dir,i,j, visits[n][n], dirs[n][n];

  for(i=0;i<n;i++) for(j=0;j<n;j++) visits[i][j]=0;
  for(i=0;i<n;i++) for(j=0;j<n;j++) dirs[i][j]=0;

  dir = getPositionDir(lines, n,  pos);

  while( dir !=-1){
    dir = moveGuard(lines,n,  dir, pos);

    visits[pos[0]][pos[1]]++;
    if(print)
      printMap(lines, n);

    if(visits[pos[0]][pos[1]] >1 && dirs[pos[0]][pos[1]]==dir)
      return 1;
    dirs[pos[0]][pos[1]]=dir;
    }
  return 0;
  }
