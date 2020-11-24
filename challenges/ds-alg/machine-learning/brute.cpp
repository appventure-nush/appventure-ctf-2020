#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) cerr << #x << " :: " << x << endl
#define _ << " " <<
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for (int i=(a);i>=(b);--i)

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int N; cin >> N;
    int P[N], R[N];
    FOR(i,0,N-1){
        cin >> P[i] >> R[i];
    }

    vector<int> v;
    FOR(i,0,N-1){
        bool ok = true;
        FOR(j,0,N-1) if (j != i) {
            if (P[i] <= P[j] && R[i] <= R[j] && !(P[i]==P[j] && R[i]==R[j] && i > j)) {
                ok = false;
                break;
            }
        }
        if (ok) v.push_back(i);
    }
    cout << SZ(v) << '\n';
    for (int& x : v) cout << x << '\n';
}

