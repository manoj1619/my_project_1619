#include <stdio.h>
#include <stdlib.h>

/**
 * @brief Adds two integers.
 *
 * @param a First integer
 * @param b Second integer
 * @return Sum of a and b
 */
int add_numbers(int a, int b)
{
    return a + b;
}

/**
 * @brief Main entry point.
 *
 * @return Exit status
 */
int main(void)
{
    int num1 = 5;
    int num2 = 7;

    int sum = add_numbers(num1, num2);
    printf("Sum: %d\n", sum);

    return 0;
}
