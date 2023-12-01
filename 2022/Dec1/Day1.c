#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
// 1. Count the number of elves
//    - Read the file line by line and every blank line do +1 and print elf
// 2. Make elf class: #items, [items], [biggest item]
//    - The items is a pointer to ints. You can go through and malloc after you have #items.



struct Elf {
	int Id;
	int *food;
	int BiggestFood;
	int n_food;
};

int check_elf(struct Elf *elves, int id);

int main(){

int n_elves, n_food, n_elf, i, j;
char *line = NULL;
char input[]= "input.txt";
size_t len = 0;
ssize_t read;



FILE *fp;

n_elves = n_food = 0;

// Count Elves (This count depends on there being an empty line at end of file)
fp = fopen(input, "r");
while ( read= getline(&line, &len, fp) != -1 ) if (isspace(line[0])) n_elves++;
fclose(fp);
printf("There are %d elves\n",n_elves);

// Declare Elf array
struct Elf *elves, *elf_pt;
elf_pt = elves  = ( struct Elf * ) malloc( n_elves*sizeof(struct Elf) );

// Count food per elf.
fp = fopen(input, "r");
n_elf=n_food=0;
while ( read= getline(&line, &len, fp) != -1 ) {
    if (isspace(line[0])){
      elf_pt->Id = ++n_elf;
      elf_pt->n_food = n_food;
      printf("Elf: %d; %d items\n\n",n_elf, n_food);
      elf_pt++;
      n_food=0;                  // set food counter to zero
      }
    else{
      n_food++;
      sscanf(line, "%d", &i);
      printf("%d\n", i);
      }
    }
fclose(fp);

// Make room in elf bags for elf food
elf_pt=elves;
for (i=0;i<n_elves;i++){
  elf_pt->food = ( int* ) malloc( elf_pt->n_food*sizeof(int) );
  elf_pt++;
  }

// Fill elf bags
int *bag_ptr;
fp = fopen(input, "r");
elf_pt=elves;
bag_ptr = elf_pt->food;
while ( read= getline(&line, &len, fp) != -1 ) {
    if (isspace(line[0])){
      elf_pt++;
      bag_ptr = elf_pt->food;
      }
    else{
      sscanf(line, "%d", bag_ptr);
      bag_ptr++;
      }
    }
fclose(fp);

// Check a particular elf.
check_elf(elves, 34);

// Find elf with most calories, and how many calories that is.
int max_elf, max_cal, sum;
max_elf=max_cal=0;

for (i=0; i<n_elves;i++){
  sum=0;
  for(j=0;j<elves[i].n_food;j++)
    sum += elves[i].food[j];
  if( sum > max_cal){
    max_cal = sum;
    max_elf=i+1;
    }
  }

printf("Max elf %d has max cals %d\n",max_elf,max_cal);



return 0;

}









int check_elf( struct Elf *elves , int id)
{
  int i;
  printf("Elf: %d\n",elves[id-1].Id);
  for (i=0;i<elves[id-1].n_food;i++)
    printf("%d\n",elves[id-1].food[i]);

  return 0;
}
