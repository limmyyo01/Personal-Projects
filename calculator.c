#include <stdio.h>
#include <cs50.h>

int main(void)
{
 long firstNumber =get_long("first number? ");
 long secondNumber =get_long("second number? ");
 char symbol =get_char("symbol? ");
    if(symbol == + )
    {
       int sum = firstNumber + secondNumber;
        printf("%d\n", sum);
    }
    else if (symbol == -)
    {
        int min = firsstNumber - secondNumber;
        printf("%d\n", min);
    }else if (symbol == * )
    {
        int times = firstNumber*secondNumber;
        printf("%d\n", times);
    }else if (symbol == /)
    {
        int div = firstNumber/secondNumber;
        printf("%d\n", div);
    }else
        printf("invalid input");
}
