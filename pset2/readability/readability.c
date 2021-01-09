#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main(void)
{
    int letters = 0;
    int words = 1;
    int sentences = 0;
    int index;
    float lForm;
    float sForm;

    string text = get_string("Text\n");
    int n = strlen(text);
    for (int i = 0; i < n; i++)
    {
        // count the number of letters.
        if (isalpha(text[i]))
        {
            letters++;
        }
        // count the number of words.
        if (text[i] == ' ')
        {
            words++;
        }
        // count the number of sentences.
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }
    // calculate index using Coleman-Liau formula.
    lForm = (float) letters / words * 100;
    sForm = (float) sentences / words * 100;
    index = round((0.0588 * lForm) - (0.296 * sForm) - 15.8);

    // If Coleman -Lau Index is less than 1, print as below.
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    // If Coleman -Lau Index is 16 or more, print as below.
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    // If Coleman -Lau Index is between 1-16, print as below.
    else
    {
        printf("Grade %d\n", index);
    }
}
