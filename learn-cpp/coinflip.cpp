#include <iostream>
#include <stdlib.h>
#include <ctime>

int main()
{
    // Createw a number that is `0` or `1`.
    srand(time(NULL));
    int coin = rand() % 2;

    // 0: Heads | 1: Tails
    if (coin == 0)
    {
        std::cout << "Heads\n";
    }
    else
    {
        std::cout << "Tails\n";
    }
}
