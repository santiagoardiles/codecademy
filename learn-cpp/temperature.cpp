#include <iostream>

int main()
{
    double tempf;
    double tempc;

    // Gets input from the user.
    std::cout << "Enter the temperature in Fahrenheit: ";
    std::cin >> tempf;

    tempc = (tempf - 32) / 1.8;

    std::cout << "The temperature is " << tempc << " degrees Celsius.\n";
}
