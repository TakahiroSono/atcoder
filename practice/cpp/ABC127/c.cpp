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
    int n, m;
    cin >> n >> m;

    int l = 0, r = 110000;

    for (size_t i = 0; i < m; i++)
    {
        int il, ir;
        cin >> il >> ir;

        l = max(l, il);
        r = min(r, ir);
    }

    if (l > r) cout << 0 << endl;
    else cout << r - l + 1 << endl;
    return 0;
}
