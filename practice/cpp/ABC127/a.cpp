#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
const int mod = 1e9+7;
const double PI = 3.1415926535;
const ll INF = 1LL << 60;

int main(int argc, char const *argv[])
{
    int a, b;
    cin >> a >> b;

    if (a >= 13) cout << b << endl;
    else if (13 > a && a > 5) cout << b / 2 << endl;
    else cout << 0 << endl;
    return 0;
}
