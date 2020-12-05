#include <iostream>
#include <stdlib.h>
#include <string>

int main()
{
    int planet;
    double weight;
    std::string planet_name;

    // Change to "cls" for Windows.
    system("clear");

    std::cout << "Enter you weight on Earth: ";
    std::cin >> weight;

    std::cout << "\nI have information for the following planets:\n\n";
    std::cout << "   1. Mercury   2. Venus    3. Mars\n";
    std::cout << "   4. Jupiter   5. Saturn   6. Uranus\n";
    std::cout << "   7. Neptune\n\n";

    std::cout << "Which planet are you visiting? ";
    std::cin >> planet;

    switch (planet)
    {
    case 1:
        weight = weight * 0.38;
        planet_name = "Mercury";
        break;

    case 2:
        weight = weight * 0.91;
        planet_name = "Venus";
        break;

    case 3:
        weight = weight * 0.38;
        planet_name = "Mars";
        break;

    case 4:
        weight = weight * 2.34;
        planet_name = "Jupiter";
        break;

    case 5:
        weight = weight * 1.06;
        planet_name = "Saturn";
        break;

    case 6:
        weight = weight * 0.92;
        planet_name = "Uranus";
        break;

    case 7:
        weight = weight * 1.19;
        planet_name = "Neptune";
        break;

    default:
        std::cout << "Invalid input.\n";
        return 0;
    }

    std::cout << "\nYour weight in " << planet_name << " is " << weight << " units.\n\n\n";
}
