#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

const int MAXN = 1003;
int n, C;
int v[MAXN];
int w[MAXN];

int dp[MAXN][MAXN];

int zero_one() {
    for (int cap = 1; cap <= C; ++cap) {
        for (int i = 1; i <= n; ++i) {
            dp[i][cap] = dp[i - 1][cap];
            if (w[i - 1] <= cap) {
                dp[i][cap] = max(dp[i][cap], v[i - 1] + dp[i - 1][cap - w[i - 1]]);
            }
        }
    }

    return dp[n][C];
}

int infinite() {
    dp[n][0] = 0;
    for (int cap = 1; cap <= C; ++cap) {
        for (int i = 0; i < n; ++i) {
            if (w[i] <= cap) {
                dp[n][cap] = max(dp[n][cap], dp[n][cap - w[i]] + v[i]);
            }
        }
    }

    return dp[n][C];
}

double fractional() {
    vector<pair<int, int> > jewels;
    for (int i = 0; i < n; ++i) {
        jewels.push_back({v[i], w[i]});
    }

    sort(jewels.begin(), jewels.end(), [](const pair<int, int> a, const pair<int, int> b) {
        return a.first * b.second < b.first * a.second;
    });

    reverse(jewels.begin(), jewels.end());
    double cap = C;
    double value = 0.0;

    for (int i = 0; i < n; ++i) {
        double taken = min((double) jewels[i].second, cap);
        value += taken * jewels[i].first / jewels[i].second;

        cap -= taken;
    }

    return value;
}

double lol() {
    double bestRatio = v[0] / w[0];
    for (int i = 0; i < n; ++i) {
        bestRatio = max(bestRatio, ((double) v[i]) / w[i]);
    }

    return bestRatio * C;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T-- > 0) {
        scanf("%d %d", &n, &C);

        for (int i = 0; i < n; ++i) {
            scanf("%d %d", v + i, w + i);
        }

        int one = zero_one();
        int two = infinite();
        double three = fractional();
        double four = lol();

        printf("%d %d %.2f %.2f\n", one, two, three, four);
    }

    return 0;
}
