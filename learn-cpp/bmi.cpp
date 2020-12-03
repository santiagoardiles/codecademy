#include <iostream>

int main()
{
    double height, weight, bmi;

    // Asks the user for their height.
    std::cout << "Type in your height (m): ";
    std::cin >> height;

    // Asks the user for their weight.
    std::cout << "Type in your weight (kg): ";
    std::cin >> weight;

    // Calculates BMI.
    bmi = weight / (height * height);
    std::cout << "Your BMI is " << bmi << "\n";

    return 0;
}
