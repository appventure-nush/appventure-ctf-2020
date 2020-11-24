#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) cerr << #x << " :: " << x << endl
#define _ << " " <<
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for (int i=(a);i>=(b);--i)

const int mxN = 5e6+5;
const int mxPR = 5e6+5;

int N, P[mxN], R[mxN];
queue<int> q[mxPR];
int stk[mxN];   // stl stack is slow
bool ans[mxN];

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> N;
    FOR(i,0,N-1){
        cin >> P[i] >> R[i];
        q[P[i]].push(i);
    }

    int ptr = 0;
    FOR(i,0,mxPR-1) while (SZ(q[i])) {
        int x = q[i].front(); q[i].pop();
        while (ptr > 0 && R[stk[ptr-1]] <= R[x]) --ptr;
        if (ptr > 0 && P[stk[ptr-1]] == P[x]) continue;
        stk[ptr++] = x;
    }

    FOR(i,0,ptr-1) ans[stk[i]] = 1;
    cout << ptr << '\n';
    FOR(i,0,N-1) if (ans[i]) cout << i << '\n';
}

