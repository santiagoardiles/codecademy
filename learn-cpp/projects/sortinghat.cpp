#include <iostream>
#include <string>

int main()
{
    int gryffindor = 0;
    int hufflepuff = 0;
    int ravenclaw = 0;
    int slytherin = 0;

    int answer1, answer2, answer3, answer4;

    std::cout << "\n\n\n\nThe Sorting Hat Quiz!\n";

    // ---------- First question. ---------- //
    std::cout << "\nQ1) When I'm dead, I want people to remember me as:\n\n";
    std::cout << "     1) The Good     2) The Great\n";
    std::cout << "     3) The Wise     4) The Bold\n";
    std::cin >> answer1;

    switch (answer1)
    {
    case 1:
        hufflepuff++;
        break;
    case 2:
        slytherin++;
        break;
    case 3:
        ravenclaw++;
        break;
    case 4:
        gryffindor++;
        break;
    default:
        std::cout << "Invalid input.\n";
        return 0;
    }

    // ---------- Second question. ---------- //
    std::cout << "\nQ2) Dawn or Dusk?\n\n";
    std::cout << "     1) Dawn     2) Dusk\n";
    std::cin >> answer2;

    switch (answer2)
    {
    case 1:
        gryffindor++;
        ravenclaw++;
        break;
    case 2:
        hufflepuff++;
        slytherin++;
        break;
    default:
        std::cout << "Invalid input.\n";
        return 0;
    }

    // ---------- Third question. ---------- //
    std::cout << "\nWhich kind of instrument most pleases your ear?\n\n";
    std::cout << "     1) The violin     2) The trumpet\n";
    std::cout << "     3) The piano      4) The drum\n";
    std::cin >> answer3;

    switch (answer3)
    {
    case 1:
        hufflepuff++;
        break;
    case 2:
        slytherin++;
        break;
    case 3:
        ravenclaw++;
        break;
    case 4:
        gryffindor++;
        break;
    default:
        std::cout << "Invalid input.\n";
        return 0;
    }

    // ---------- Fourth question. ---------- //
    std::cout << "\nQ4) Which road tempts you most?\n\n";
    std::cout << "     1) The wide, sunny grassy lane\n";
    std::cout << "     2) The narrow, dark, lantern-lit alley\n";
    std::cout << "     3) The twisting, leaf-strewn path through woods\n";
    std::cout << "     4) The cobbled street lined (ancient buildings)\n";
    std::cin >> answer4;

    switch (answer4)
    {
    case 1:
        hufflepuff++;
        break;
    case 2:
        slytherin++;
        break;
    case 3:
        gryffindor++;
        break;
    case 4:
        ravenclaw++;
        break;
    default:
        std::cout << "Invalid input.\n";
        return 0;
    }

    // ---------- Sorting. ---------- //
    std::string house;
    int max = 0;

    std::cout << "\n\nCongrats on being sorted into... ";

    if (gryffindor > max)
    {
        max = gryffindor;
        house = "Gryffindor";
    }

    if (hufflepuff > max)
    {
        max = hufflepuff;
        house = "Hufflepuff";
    }

    if (ravenclaw > max)
    {
        max = ravenclaw;
        house = "Ravenclaw";
    }

    if (slytherin > max)
    {
        max = slytherin;
        house = "Slytherin";
    }

    std::cout << house << "!\n\n";
}