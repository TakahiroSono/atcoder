#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
using ll = long long;
using P = pair<ll, ll>;

const int MOD = 1e9+7;
const double PI = 3.1415926535;
const ll INF = 1LL << 60;

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;

    vector<int> w(n);
    for(int i = 0; i < n; ++i) cin >> w[i];

    vector<int> sum_w(n), re_w(n);
    sum_w[0] = w[0];
    re_w[n-1] = w[n-1];
    for(int i = 1; i < n; ++i) {
        sum_w[i] = w[i] + sum_w[i-1];

    }
    for (int i = n-2; i >= 0; i--)
    {
        re_w[i] = w[i] + re_w[i+1];
    }

    int minimum = 100 * 100;
    for(int i = 1; i < n; ++i) {
        int m = abs(sum_w[i-1] - re_w[i]);
        if (minimum > m)
        {
            minimum = m;
        }
    }
    cout << minimum << endl;
    return 0;
}
