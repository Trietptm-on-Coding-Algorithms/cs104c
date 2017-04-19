#include <iostream>
#include <cstring>

using namespace std;

const int MOD = 1000000007;
int change[] = {1, 5, 10, 25};

long long dp[1003];

void gen_dp() {
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    for (int i = 1; i <= 1000; ++i) {
        dp[i] = 0;
        for (int j = 0; j < 4; ++j) {
            if (change[j] <= i) {
                dp[i] += dp[i - change[j]];
                dp[i] %= MOD;
            }
        }
    }
}

int main() {
    gen_dp();

    int T, x;
    cin >> T;

    while (T-- > 0) {
        cin >> x;
        cout << dp[x] << '\n';
    }

    return 0;
}
