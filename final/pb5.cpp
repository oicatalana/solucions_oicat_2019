#include <iostream>
#include <vector>
#include <map>
using namespace std;

vector<int> monedes{1, 2, 5, 10, 20, 50, 100, 200};
map<int, int> formes;

void rec(int pos, int suma)
{
    if (pos == monedes.size())
        ++formes[suma];
    else
    {
        rec(pos + 1, suma);
        rec(pos + 1, suma + monedes[pos]);
        rec(pos + 1, suma + monedes[pos]);
        rec(pos + 1, suma + 2 * monedes[pos]);
    }
}

int main()
{
    rec(0, 0);

    int maxim = 0;
    int suma = 0;
    for (auto [suma_loc, maneres] : formes)
    {
        if (maxim < maneres)
        {
            maxim = maneres;
            suma = suma_loc;
        }
    }

    cout << suma << "-" << maxim << endl;
}
