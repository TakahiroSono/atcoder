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
    int a, b, c;
    cin >> a >> b >> c;

    if (a + b >= c) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
    return 0;
}
