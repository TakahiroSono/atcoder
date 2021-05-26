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
    ll n, m;
    cin >> n >> m;

    vector<ll> a(m+1);
    for(int i = 0; i < m; ++i) cin >> a[i];

    vector<ll> dp(n+1);

    ll cnt = 0;

    dp[0] = 1;
    if (a[0] != 1) dp[1] = 1;
    else cnt++;

    for (size_t i = 2; i < n+1; i++)
    {
        if (a[cnt] == i)
        {
            dp[i] = 0;
            cnt++;
            continue;
        }

        dp[i] = (dp[i-1] + dp[i-2]) % MOD;
    }

    cout << dp[n] << endl;
    return 0;
}
