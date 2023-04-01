#include <stdio.h>
#include <cs50.h>
int main (void)
{
    string firstnum = get_string ("input first number ?");
    string secondnum = get_string("input second number ?");
    printf("%s + ,%s" firstnum, secondnum);
}