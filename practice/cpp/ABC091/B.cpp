#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;
const int mod = 1e9+7;
const double PI = 3.1415926535;
const ll INF = 1LL << 60;

int main(int argc, char const *argv[])
{
    int n, m;

    map<string, int> s, t;

    cin >> n;
    for (size_t i = 0; i < n; i++)
    {
        string w;
        cin >> w;
        auto it = s.find(w);
        if(it != s.end()) s[w] += 1;
        else s[w] = 1;
    }

    cin >> m;
    for (size_t i = 0; i < m; i++)
    {
        string w;
        cin >> w;
        auto it = t.find(w);
        if(it != t.end()) t[w] += 1;
        else t[w] = 1;
    }

    int ans = 0;
    for(auto it = s.begin(); it != s.end(); it++) {
        ans = max(ans, it->second - t[it->first]);
    }
    cout << ans << endl;
    return 0;
}
