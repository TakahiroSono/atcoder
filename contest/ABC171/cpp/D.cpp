#include <iostream>
#include <set>
#include <map>
using namespace std;

int main(int argc, char const *argv[])
{
  long long int N, Q;
  long long int A[110000], B[110000], C[110000];
  std::map<int, int> mp;

  cin >> N;
  for (int i=0; i < N; i++){
    cin >> A[i];
    auto itr = mp.find(A[i]);
    if (itr != mp.end()) {
      mp[A[i]] += 1;
    } else
    {
      mp[A[i]] = 1;
    }
  }

  cin >> Q;
  long long int ans;
  for (int i = 0; i < Q; i++){
    cin >> B[i] >> C[i];
    auto itr = mp.find(B[i]);
    if (itr != mp.end()) {
      mp[C[i]] += mp[B[i]];
      mp[B[i]] = 0;
    }
    ans = 0;
    for (auto itr = mp.begin(); itr != mp.end(); ++itr){
      ans += itr->first * itr->second;
    }
    cout << ans << endl;
  }
  return 0;
}
