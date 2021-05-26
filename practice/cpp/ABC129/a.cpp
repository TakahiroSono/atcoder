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
    int p, q, r;
    cin >> p >> q >> r;

    int ans = 0;
    vector<int> array = {p, q, r};
    sort(array.begin(), array.end());

    ans += array[0] + array[1];

    cout << ans << endl;

    return 0;
}
