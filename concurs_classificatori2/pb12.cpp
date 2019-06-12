#include <iostream>
#include <vector>
#include <set>
using namespace std;


const int MOD = 32749;


const vector<string> color = { "B", "G", "R", "Y" };
const vector<string> simbol = { "canvi", "torn", "dues" };


using P = pair<int, int>;
using SP = multiset<P, greater<P>>;
using VSP = vector<SP>;


int seed;
VSP S;
P top;
int jug, inc;


void seg() {
  seed = (97*seed + 20)%MOD;
}


P carta() {
  P c;
  seg();
  c.second = seed%4;
  seg();
  c.first = seed%13;
  return c;
}


void print(int i) {
  cout << "el jugador " << char('A' + i);
}


void print(P c) {
  cout << "(" << color[c.second] << ", ";
  int f = c.first;
  if (f < 10) cout << f;
  else cout << simbol[f-10];
  cout << ")";
}


bool encaixen(P a, P b) {
  return a.first == b.first or a.second == b.second;
}


void next() {
  jug = (jug + inc + 4)%4;
}


P roba() {
  print(jug);
  cout << " roba ";
  P c = carta();
  print(c);
  cout << endl;
  S[jug].insert(c);
  return c;
}


bool juga() {
  auto p = S[jug].begin();
  while (p != S[jug].end() and not encaixen(top, *p)) ++p;
  P c;
  if (p != S[jug].end()) c = *p;
  else {
    c = roba();
    if (not encaixen(top, c)) {
      print(jug);
      cout << " passa";
      cout << endl;
      next();
      return true;
    }
  }

  print(jug);
  cout << " juga ";
  print(c);
  cout << endl;
  S[jug].erase(S[jug].find(c));
  top = c;

  if (S[jug].empty()) return false;

  if (c.first == 12) {
    next();
    roba();
    roba();
  }
  else if (c.first == 11) next();
  else if (c.first == 10) inc = -inc;
  next();
  return true;
}


int main() {
  cin >> seed;
  S = VSP(4);
  for (int i = 0; i < 4; ++i) {
    print(i);
    cout << " rep ";
    for (int j = 0; j < 7; ++j) {
      cout << (j ? ", " : "");
      P c = carta();
      print(c);
      S[i].insert(c);
    }
    cout << endl;
  }
  cout << "la carta a la taula es ";
  top = carta();
  print(top);
  cout << endl;
  jug = 0;
  inc = 1;
  while (juga()) ;
}