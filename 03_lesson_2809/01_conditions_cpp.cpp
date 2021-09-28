#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "Введите число: " << endl;
    cin >> number;

    if (number % 5 == 0) {
        cout << "Число делится на 5!" << endl;
                        cout << "Молодец!" << endl;
    }
    else {
        cout << "Число НЕ делится на 5!" << endl;
    }
    return 0;
}
