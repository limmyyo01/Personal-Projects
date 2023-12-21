#include <stdio.h>
#include <cs50.h>

int main(void)
{
 int firstNumber =get_int("first number? ");
 int secondNumber =get_int("second number? ");
 char symbol =get_int("symbol?\n ");
    if(symbol == '+')
    {
        int sum = (firstNumber + secondNumber);
        printf("%d\n", sum);
    }
}
