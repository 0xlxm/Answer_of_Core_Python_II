#include<stdio.h>

void reverse(const char * const sPtr);

int main ()
{
    char sentence[80];
    printf("Input a line:\n");
    gets(sentence);

    printf("after reverse line: \n");
    reverse(sentence);

    printf("\n");
    system("pause");
    return 0;
}

void reverse(const char * const sPtr)
{
    if(sPtr[0] == '\0')
    {
        return ;
    }

    else
    {
        puts(sPtr);
        reverse(&sPtr[1]); 
        putchar(sPtr[0]);
    }
}
