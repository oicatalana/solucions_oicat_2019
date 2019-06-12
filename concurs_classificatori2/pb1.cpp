#include <iostream>
#include <vector>
using namespace std;

int monedes[] = {1, 2, 5, 10, 20, 50};
vector<vector<int>> sols;

void rec(vector<int>&v, int i)
{
    if (i == 6)
    {
        sols.push_back(v);
        return;
    }

    if (v.size() < 8)
    {
        v.push_back(monedes[i]);
        rec(v, i);
        v.pop_back();
    }

    rec(v, i + 1);
}

int main()
{
    vector<int> v;
    rec(v, 0);

    for (vector<int> const& sol : sols)
    {
        bool ok = true;
        for (int i = 0; i < 100 && ok; ++i)
        {
            bool found = false;
            for (int j = 0; j < (1 << sol.size()) && !found; ++j)
            {
                int sum = 0;
                for (int k = 0; k < sol.size(); ++k)
                    if ((j >> k) & 1)
                        sum += sol[k];
                if (sum == i)
                    found = true;
            }

            if (!found)
                ok = false;
        }

        if (ok)
        {
            for (int i = 0; i < sol.size(); ++i)
                cout << sol[i] << " ";
            cout << endl;
        }
    }
}