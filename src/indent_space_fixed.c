#include <stdio.h>

#define MAXVAL 100

/**
 * @brief Adds two integers.
 * @param a First integer
 * @param b Second integer
 * @return Sum of a and b
 */
int add(int a, int b) { return a + b; }

/**
 * @brief Main program entry point.
 *
 * @return int Returns the sum of two integers.
 */
int main() {
  int x;
  int y = 20;

  printf("Enter a value for x: ");
  scanf("%d", &x);

  if (x > 5) {
    printf("X is greater than 5\n");
  } else {
    printf("X is not greater than 5\n");
  }

  return add(x, y);
}
