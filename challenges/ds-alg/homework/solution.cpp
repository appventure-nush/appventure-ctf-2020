#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef pair<ii, int> ri3;
#define mp make_pair
#define pb push_back
#define fi first
#define sc second
#define sz(x) (int)(x).size()
#define all(x) begin(x), end(x) 
#define rep(i, n) for (int i = 0; i < n; ++i) 
#define fo(i, a, b) for (int i = a; i <= b; ++i)

int main() {
    //freopen("in.txt", "r", stdin);
    int t; scanf("%d", &t);
    fo(tc, 1, t) {
        int n, m, l; scanf("%d%d%d", &n, &m, &l);
        vector<pair<int, string> > v;
        for (int i = 0; i < l; ++i) {
            char name[20]; int a, b; scanf(" %[^:]:%d,%d", &name, &a, &b);
            int x = n, y = m;
            int cost = 0;
            while (x > y) {
                if (x/2 >= y) {
                    int dec = x - x/2;
                    cost += min(dec*a, b);
                    x /= 2;
                }
                else {
                    cost += (x-y)*a;
                    x = y;
                }
            }
            v.push_back(make_pair(cost, name));
        }
        sort(all(v));
        printf("Case %d\n", tc);
        for (auto x : v) {
            printf("%s %d\n", x.sc.c_str(), x.fi);
        }
    }
}

