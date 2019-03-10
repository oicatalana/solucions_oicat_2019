#include <iostream>
using namespace std;


int main() {
    int n;
    cin >> n;
    int suma = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char d;
            cin >> d;
            if (i == j or i == n - j - 1) suma += d - '0';
        }
    }
    cout << suma << endl;
}
