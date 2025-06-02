#include <stdio.h>

int main() {
  int x = 10;
  int y = 20;
  if (x == y) {    // Missing spaces around 'if', '==', and inside brackets
    int z = x + y; // Missing spaces around '=' and '+'
    printf("Sum: %d\n", z);
  }

  return 0;
}
