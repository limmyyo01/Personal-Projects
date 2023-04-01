#include <stdio.h>
#include <cs50.h>
int main (void)
{
    int firstnum = get_int ("input first number ?");
    int secondnum = get_int ("input second number ?");
    int result = get_int ( firstnum + secondnum )
    printf("%i + %i == result", firstnum, secondnum);
}