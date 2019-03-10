#include <iostream>
#include <string>
using namespace std;


int main() {
    string noma, nomb, nomc;
    int a, b, c;
    cin >> noma >> a >> nomb >> b >> nomc >> c;

    if (a < b and a < c) cout << noma << endl;
    else if (b < c) cout << nomb << endl;
    else cout << nomc << endl;
}
