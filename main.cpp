#include <iostream>
using namespace std;

int main() {
    std::cout << "Привет, мир!" << std::endl;

    std::string name;
    std::cout << "Как тебя зовут? ";
    std::cin >> name;
    std::cout << "Привет, " << name << "!" << std::endl;

    return 0;
}
