#include <iostream>

int main()
{
    double pesos, reais, soles, dollars;

    std::cout << "Enter number of Colombian Pesos: ";
    std::cin >> pesos;

    std::cout << "Enter number of Brazilian Reais: ";
    std::cin >> reais;

    std::cout << "Enter number of Peruvian Soles: ";
    std::cin >> soles;

    dollars = (0.00028 * pesos) + (0.19 * reais) + (0.28 * soles);
    std::cout << "US Dollars = $ " << dollars << "\n";
}
