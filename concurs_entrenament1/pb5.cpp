#include <iostream>
using namespace std;


int main() {
  int n;
  cin >> n;
  if (n > 30) cout << "fa calor" << endl;
  else if (n < 10) cout << "fa fred" << endl;
  else cout << "s'esta be" << endl;
  if (n >= 100) cout << "l'aigua bulliria" << endl;
  else if (n <= 0) cout << "l'aigua es gelaria" << endl;
}
