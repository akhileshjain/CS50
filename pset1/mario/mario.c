#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int height = get_positive_int();
    for (int i = 1; i <= height; i++)
    {
        for (int k = height; k > i; k--)
        {
            // print spaces
            printf(" ");
        }
        for (int j = height; j > height - i; j--)
        {
            // print hashes
            printf("#");
        }
        printf("  ");
        for (int l = height; l > height - i; l--)
        {
            printf("#");
        }
        // Move over next line
        printf("\n");
    }
}

int get_positive_int(void)
{

    int n;
    do
    {
        n = get_int("Height\n");
    }
    while (n < 1 || n > 8);
    return n; // Keep asking for input if not in range 1-8 (inclusive)

}