#include <iostream>
using namespace std;

int main() 
{
    int x;
    cin >> x;
    int i = 1;
    while (i <= 10) 
    {
        cout << x << "*" << i << " = " << x*i << endl;
        ++i;
    }
}
