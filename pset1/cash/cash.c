#include <stdio.h>
#include <cs50.h>
#include <math.h>

float get_positive_float(void);

int main(void)
{
    float dollar = get_positive_float();
    // convert dollar to cents to avoid floating point precision error
    int cent = round(dollar * 100);
    // count variable to keep count of coins
    int count = 0;
    // Loop for getting count of 25 cent coins
    while (cent >= 25)
    {
        count++;
        cent = cent - 25;
    }
    // Loop for getting count of 10 cent coins
    while (cent >= 10 && cent < 25)
    {
        count++;
        cent = cent - 10;
    }
    // Loop for getting count of 5 cent coins
    while (cent >= 5 && cent < 10)
    {
        count++;
        cent = cent - 5;
    }
    // Loop for getting count of 1 cent coins
    while (cent >= 1 && cent < 5)
    {
        count++;
        cent = cent - 1;
    }
    printf("%i", count);
}

float get_positive_float(void)
{
    // Keeping asking for input till user does not enter a positive number.
    float n;
    do
    {
        n = get_float("Change owed:\n");
    }
    while (n < 0.0);
    return n;
}