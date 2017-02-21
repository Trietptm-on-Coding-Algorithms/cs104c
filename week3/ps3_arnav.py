def run(poly, x, y):
    base = 1
    ans = 0
    for coeff in poly:
        ans += coeff * base
        base *= x
        if ans > y:
            return ans

    return ans

def main():
    n, y = map(int, input().split())
    poly = list(map(int, input().split()))
    if run(poly, 0, y) == y:
        print(0)
    else:
        lo = 1
        hi = 2
        while run(poly, hi, y) <= y:
            lo *= 2
            hi *= 2

        # eval(lo) <= y
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if run(poly, mid, y) <= y:
                lo = mid
            else:
                hi = mid

        if run(poly, lo, y) == y:
            print(lo)
        else:
            print(-1)

t = int(input())
for _ in range(t):
    main()
