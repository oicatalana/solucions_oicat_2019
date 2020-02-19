#include <iostream>
#include <map>
using namespace std;

int main()
{
    map<int, int> quantitat;

    for (int i = 1; i <= 100; ++i)
    {
        for (int j = i; j <= 100; ++j)
        {
            int x = i * i * i + j * j * j;
            if (x < 1000000)
                ++quantitat[x];
        }
    }

    int resposta;
    for (auto [x, formes] : quantitat)
        if (formes >= 2)
            resposta = x;

    cout << resposta << endl;
}
