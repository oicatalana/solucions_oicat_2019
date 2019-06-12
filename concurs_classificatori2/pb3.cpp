#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{
    map<pair<int, int>, int> pos;
    int a = 99, b = 98;
    int count = 2;
    while (true)
    {
        int c = (a * b) % 100;
        ++count;
        a = b;
        b = c;
        std::cout << count << " " << a << " " << b << endl;
        if (!pos.count(make_pair(a, b)))
        {
            pos[make_pair(a, b)] = count;
        }
        else
        {
            cout << a << " " << b << " " << pos[make_pair(a, b)] << " " << count << endl;
            break;
        }
    } 
}