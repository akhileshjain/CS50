#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // get_string is a function provided by CS50 lib.
    string name = get_string("What is your name\n");
    printf("hello, %s\n", name); // prints hello, followed by name input via command line.
}