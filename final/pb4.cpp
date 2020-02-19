#include <iostream>
using namespace std;

int main()
{
    int maxim = 0;
    for (int x = 0; x < 1 << 25; ++x)
    {
        int sum = 0;
        int actual = x;
        for (int i = 1; i <= 25; ++i)
        {
            sum += __builtin_popcount(actual);
            actual = (actual ^ (actual >> 1)) & ~(1 << (25 - i));
        }

        maxim = max(maxim, sum);
    }

    cout << maxim << endl;
}
