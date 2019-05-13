#include <iostream>
using namespace std;


const int MAX = 1e5;


int main() {
  string s = "0";
  while ((int)s.size() < MAX) {
    string t;
    for (char c : s) t += '0' + (1 - (c - '0'));
    s += t;
  }

  int n;
  while (cin >> n) cout << s.substr(0, n) << endl;
}
