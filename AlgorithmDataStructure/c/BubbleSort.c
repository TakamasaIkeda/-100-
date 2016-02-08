#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 10
int sort[N];
void BubbleSort(void);
void RandomList(void);


int main(void){
  int i;
  printf("before sort\n");
  RandomList(); 
  for(i=0; i< N; i++){
    printf("%d\n", sort[i]);
  }
  printf("\n");
  BubbleSort();
  printf("after sort\n");
  for(i=0; i< N; i++){
    printf("%d\n", sort[i]);
  }
  
  return 0;
}

//create random ten length list
void RandomList(void){
  srand((unsigned int)time(NULL));

  int i;
  for(i=0; i<N; i++){
    sort[i] = rand();
  }
}

//bubble sort
void BubbleSort(void){
  int i, j, flag;

  do{
    flag = 0;
    for(i=0; i<N; i++){
      if(sort[i] > sort[i+1]){
        j = sort[i];
        sort[i] = sort[i+1];
        sort[i+1] = j;

        flag = 1;
      }
    }
  }while(flag==1);
}
