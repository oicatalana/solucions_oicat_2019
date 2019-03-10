#include<iostream>
#include<string>
#include<vector>
using namespace std;


typedef vector<char> Fila;
typedef vector<Fila> Matriu;


int simula(Matriu& m, int i, int j, string s) {
    int suma = 0;
    for (int k = 0; k < s.size(); ++k) {
        if (s[k] == 'N') --i;
        else if (s[k] == 'S') ++i;
        else if (s[k] == 'E') ++j;
        else --j;
        if (m[i][j] == 'B') return suma;
        if (m[i][j] != '.') {
            suma += m[i][j] - '0';
            m[i][j] = '.';
        }
    }
    return suma;
}


int main() {
    int f, c;
    while (cin >> f >> c) {
        Matriu m(f, Fila(c));
        for (int i = 0; i < f; ++i) {
            for (int j = 0; j < c; ++j) cin >> m[i][j];
        }
        int i, j;
        string s;
        cin >> i >> j >> s;
        cout << simula(m, i, j, s) << endl;
    }
}

