#include<stdlib.h>
#include<stdio.h>
#include "../funcs.h"

struct Point {
  int x; int y;
};
struct AntennaPair {
  struct Point ant1;
  struct Point ant2;
  int dx, dy;
};

int cntAntennae(char **lines, int n);
int getAntennae(char **lines, int n, int antCnt, struct Point *Antennae);
int cntAntennaPairs(char** lines, int nAnts, struct Point *antennae);
int getAntennaPairs(char** lines, int nAnts, struct Point *antennae, struct AntennaPair *antPairs );
int calcNodes(char **lines, struct AntennaPair antPair, int n);
int calcNudes(char **lines, struct AntennaPair antPair, int n, int up);


int main(){
  FILE *file;
  int i,j,k,n,dir, nAnts,x1,y1,x2,y2;
  i=j=k=n=dir=nAnts=0;

  file = fopen("input.txt","r"); n=50;

  char **lines = (char **)malloc(n * sizeof(char *));
  for (i=0; i<n; i++) lines[i] = (char *)malloc(n * sizeof(char));
  for (i=0; i<n; i++) for(j=0;j<n;j++) lines[i][j]=' ';

  readGrid(n, lines, file);
  printMap(lines, n);

  nAnts = cntAntennae(lines,n);
  printf("There are %d antennae\n",nAnts);

  struct Point antennae[nAnts];
  getAntennae(lines, n, nAnts, antennae);

  for(i=0;i<nAnts;i++)
    printf("%d: (%d %d) %c\n",i, antennae[i].x,antennae[i].y,lines[antennae[i].x][antennae[i].y]);

  int nPairs = cntAntennaPairs(lines, nAnts, antennae);
  printf("There are %d valid antenna pairs\n",nPairs);

  struct AntennaPair antPairs[nPairs];


  int nodeCount=0;
  getAntennaPairs(lines, nAnts, antennae, antPairs );
  for(i=0;i<nPairs;i++){
    x1=antPairs[i].ant1.x;
    y1=antPairs[i].ant1.y;
    x2=antPairs[i].ant2.x;
    y2=antPairs[i].ant2.y;
    printf("(%d,%d) (%d,%d) (%d,%d) (%c,%c)\n", x1,y1,x2,y2, antPairs[i].dx, antPairs[i].dy,
      lines[x1][y1],lines[x2][y2]);
    //nodeCount += calcNodes(lines, antPairs[i], n);
    nodeCount += calcNudes(lines, antPairs[i], n,1);
    nodeCount += calcNudes(lines, antPairs[i], n,-1);
    }
  printf("\n\n");
  printMap(lines,n);
  printf("Node Count: %d\n",nodeCount);



  return 0;


}


int cntAntennae(char **lines, int n){
  int cnt=0;
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
      if(lines[i][j] > '.')
        cnt++;
  return cnt;
}



int getAntennae(char **lines, int n, int antCnt, struct Point *Antennae){
  int k=0;
  for(int i=0;i<n;i++){
    if(k==antCnt) break;
    for(int j=0;j<n;j++){
      if(lines[i][j] > '.'){
        Antennae[k].x= i; Antennae[k].y= j;
        k++;
        }
      if(k==antCnt) break;
      }
    }
  return k;
}


int cntAntennaPairs(char** lines, int nAnts, struct Point *antennae){
  int x1, y1, x2, y2,cnt;
  cnt=0;
  for(int i=0;i<nAnts;i++){
    for(int j=i+1;j<nAnts;j++){
      x1=antennae[i].x; y1=antennae[i].y;
      x2=antennae[j].x; y2=antennae[j].y;
      if(lines[x1][y1]==lines[x2][y2])
        cnt++;
      }
    }
  return cnt;
}


int getAntennaPairs(char** lines, int nAnts, struct Point *ants, struct AntennaPair *antPairs){
  int x1, y1, x2, y2,k;
  k=0;
  for(int i=0;i<nAnts;i++)
    for(int j=i+1;j<nAnts;j++){
      x1=ants[i].x; y1=ants[i].y;
      x2=ants[j].x; y2=ants[j].y;
      if(lines[x1][y1]==lines[x2][y2]){
        antPairs[k].ant1 = ants[i];
        antPairs[k].ant2 = ants[j];
        antPairs[k].dx = ants[j].x - ants[i].x;
        antPairs[k].dy = ants[j].y - ants[i].y;
        k++;
        }
      }
  return k;
}


int calcNodes(char **lines, struct AntennaPair antPair, int n){
  int node1x, node1y, node2x, node2y, empty1, empty2, occ1, occ2;
  int cnt;
  struct Point ant1, ant2;
  ant1 = antPair.ant1; ant2=antPair.ant2;

  empty1=empty2=occ1=occ2=cnt=0;

  struct Point node1 =  {ant1.x -antPair.dx         , ant1.y -antPair.dy         };
  struct Point node2 =  {ant2.x +antPair.dx         , ant2.y +antPair.dy         };
  struct Point bound1 = {(node1.x <n && node1.x >=0), (node1.y <n && node1.y >=0)};
  struct Point bound2 = {(node2.x <n && node2.x >=0), (node2.y <n && node2.y >=0)};


  if(bound1.x && bound1.y ){
    empty1 = lines[node1.x][node1.y]=='.';
    occ1 = lines[node1.x][node1.y] =='#';
    lines[node1.x][node1.y] = '#';
    }
  if(bound2.x && bound2.y){
    empty2 = lines[node2.x][node2.y]=='.';
    occ2 = lines[node2.x][node2.y] =='#';
    lines[node2.x][node2.y] = '#';
    }

  if(bound1.x && bound1.y )
    printf("Node at (%d %d)\n",node1.x,node1.y);
  if(bound2.x && bound2.y )
    printf("Node at (%d %d)\n",node2.x,node2.y);

  return (bound1.x && bound1.y && !occ1) + (bound2.x && bound2.y && !occ2);
}


int calcNudes(char **lines, struct AntennaPair antPair, int n, int up){
  int cnt, k;
  struct Point ant, node, bound;
  cnt=k=0;

  ant = antPair.ant1;
  bound.x =  bound.y = 1;
  while(bound.x && bound.y){
    node.x = ant.x + up*k*antPair.dx ;
    node.y = ant.y + up*k*antPair.dy;
    bound.x =  (node.x <n && node.x >=0);
    bound.y =  (node.y <n && node.y >=0);

    if(bound.x && bound.y && lines[node.x][node.y] !='#'){
      lines[node.x][node.y] ='#';
      cnt++;
      }
    k++;
    }
  return cnt;
}
