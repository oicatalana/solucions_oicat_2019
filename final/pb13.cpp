#include <iostream>
#include <vector>
using namespace std;


vector<string> codis_morse = {
    ".-", "-...", "-.-.", "-..", ".",
    "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---",
    ".--.", "--.-", ".-.", "...", "-", "..-",
    "...-", ".--", "-..-", "-.--", "--.."
};


string string_to_morse(const string& s) {
    string ans = "";
    for (char x : s)
        ans += codis_morse[x - 'A'];
    return ans;
}


bool es_palindrom(const string& s) {
    int n = s.size();
    for (int i = 0; 2*i < n; ++i) {
        if (s[i] != s[n - i - 1]) return false;
    }
    return true;
}


int main(){
    string s;
    while (cin >> s) {
        string t = string_to_morse(s);
        bool es_palindrom_normal = es_palindrom(s);
        bool es_palindrom_morse = es_palindrom(t);
        if (!es_palindrom_normal && !es_palindrom_morse)
            cout << "RES" << endl;
        if (es_palindrom_normal && !es_palindrom_morse)
            cout << "PALINDROM" << endl;
        if (!es_palindrom_normal && es_palindrom_morse)
            cout << "PALINDROM DE MORSE" << endl;
        if (es_palindrom_normal && es_palindrom_morse)
            cout << "SUPERPALINDROM" << endl;

    }
}
