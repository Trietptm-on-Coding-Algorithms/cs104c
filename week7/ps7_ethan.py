T = int(raw_input())
coins = [1, 5, 10, 25]

for t in range(T):
    X = int(raw_input())
    dp = [0] * (X + 1)
    dp[0] = 1

    for x in range(1, X + 1):
        for c in coins:
            if x - c >= 0:
                dp[x] += dp[x - c]
                dp[x] %= 1000000007

    print dp[X]
