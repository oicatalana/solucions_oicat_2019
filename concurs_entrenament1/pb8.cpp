#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n;
    cin >> n;
    vector<int> v(n), w(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    for (int i = 0; i < n; ++i) {
        int p;
        cin >> p;
        w[p] = v[i];
    }
    for (int i = 0; i < n - 1; ++i) cout << w[i] << ' ';
    cout << w[n - 1] << endl;
}
