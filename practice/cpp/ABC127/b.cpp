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
    int r, d, x;
    cin >> r >> d >> x;

    for (size_t i = 0; i < 10; i++)
    {
        x = r * x - d;
        cout << x << endl;
    }

    return 0;
}
