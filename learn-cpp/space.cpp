#include <iostream>

int main()
{
    double weight;
    int planet;

    std::cout << "Enter you weight on Earth: ";
    std::cin >> weight;

    std::cout << "Enter the number of the planet: ";
    std::cin >> planet;

    switch (planet)
    {
    case 1:
        weight = weight * 0.38;
        std::cout << weight;
        break;

    case 2:
        weight = weight * 0.91;
        std::cout << weight;
        break;

    case 3:
        weight = weight * 0.38;
        std::cout << weight;
        break;

    case 4:
        weight = weight * 2.34;
        std::cout << weight;
        break;

    case 5:
        weight = weight * 1.06;
        std::cout << weight;
        break;

    case 6:
        weight = weight * 0.92;
        std::cout << weight;
        break;

    case 7:
        weight = weight * 1.19;
        std::cout << weight;
        break;

    default:
        std::cout << "Invalid input.\n";
        break;
    }
}
