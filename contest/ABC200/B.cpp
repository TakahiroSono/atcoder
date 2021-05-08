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
    ll n;
    int k;

    cin >> n >> k;

    for (size_t i = 0; i < k; i++)
    {
        if (n % 200 == 0) {
            n /= 200;
        }
        else {
            n = n * 1000 + 200;
        }
    }

    cout << n << endl;
    return 0;
}
