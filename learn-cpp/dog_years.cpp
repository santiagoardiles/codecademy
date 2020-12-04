/*    Dog Years.    */

#include <iostream>

int main()
{
    // This is the name of my dog.
    const char *dog_name = "Suricata";

    // This is the age of my dog (Suricata) in human years.
    int dog_age = 5;

    // The first two years of a dog's life count as 21 human years.
    int early_years = 21;

    // Each following year counts a 4 human years.
    int later_years = (dog_age - 2) * 4;

    // This is the dog's age in human years.
    int human_years = early_years + later_years;

    std::cout << "My name is " << dog_name << " Woof woof, I am " << human_years << " years old in human years.\n";
}
