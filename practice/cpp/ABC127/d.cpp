#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
using ll = long long;
using P = pair<ll, ll>;

#define all(vec) vec.begin(), vec.end()

const int MOD = 1e9+7;
const double PI = 3.1415926535;
const ll INF = 1LL << 60;

int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;

    map<ll, ll> card;

    for (size_t i = 0; i < n; i++)
    {
        ll a;
        cin >> a;
        if(card.count(a)) card[a]++;
        else card.emplace(a, 1);
    }

    for (size_t i = 0; i < m; i++)
    {
        ll b, c;
        cin >> b >> c;
        if(card.count(c)) card[c] += b;
        else card.emplace(c, b);
    }

    // for (auto itr = card.begin(); itr != card.end(); itr++) {
    //     cout << itr->first << ':' << itr->second << endl;
    // }

    ll ans = 0;
    int cnt = 0;

    for(auto itr = card.rbegin(); itr != card.rend(); itr++) {
        for(size_t i = 0; i < itr->second; i++) {
            cnt++;
            ans += itr->first;
            if(cnt >= n) break;
        }
        if(cnt >= n) break;
    }

    cout << ans << endl;
    return 0;
}
