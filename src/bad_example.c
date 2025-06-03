#include "bad_example.h"

int main( )
{
int a=5;int b =  10 ;
  int sum = add(a,b);   
printf("Sum: %d\n", sum ) ; // Missing include for printf

return 0;
}

int add(int x,int y){
    int unused = 0;
return x + y;
}

