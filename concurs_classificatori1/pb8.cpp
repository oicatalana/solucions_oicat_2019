#include <iostream>
#include <vector>
using namespace std;


using VS = vector<string>;


const VS D =
{ ".__..",
  "( o>.",
  "///\\.",
  "\\V_/_"
};


const VS E =
{ "..__.",
  ".<o )",
  "./\\\\\\",
  "_\\_V/"
};


int main() {
  int n, p;
  cin >> n >> p;
  VS R(4, string(n, '.'));
  while (p--) {
    char c;
    int x;
    cin >> c >> x;
    if (c == 'D')
      for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 5; ++j) R[i][x+j] = D[i][j];
    else
      for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 5; ++j) R[i][x+j] = E[i][j];
  }
  for (int i = 0; i < 4; ++i) cout << R[i] << endl;
}

