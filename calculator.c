#include <stdio.h>
#include <cs50.h>

int main(void)
{
 long firstNumber =get_long("first number? ");
 long secondNumber =get_long("second number? ");
 char symbol =get_char("symbol? ");
    if(symbol == '+')
    {
        int sum = firstNumber + secondNumber;
        printf("%d\n", sum);
    }
}
