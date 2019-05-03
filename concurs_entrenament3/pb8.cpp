#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // Llegeix el nombre de formigues i la longitud del tunel a cada cas.
    int n, L;
    while (cin >> n >> L)
    {
        // Llegeix les posicions de cada formiga (venen en ordre).
        vector<int> v(n);
        for (int i = 0; i < n; ++i)
            cin >> v[i];

        // Llegeix els sentits (1 o -1)
        vector<int> sentit(n);
        for (int i = 0; i < n; ++i)
            cin >> sentit[i];

        // Ignorem els xocs.
        int result = 0;
        for (int i = 0; i < n; ++i)
        {
            if (sentit[i] == 1)
                result = max(result, L - v[i]);
            else
                result = max(result, v[i]);
        }

        cout << result << endl;
    }
}

