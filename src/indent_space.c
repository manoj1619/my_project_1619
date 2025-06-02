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
  int x = 10;
  int y = 20;

  if (x > 5) { // Changed condition to avoid always true warning
    printf("X is greater than 5\n");
  }

  return add(x, y);
}
