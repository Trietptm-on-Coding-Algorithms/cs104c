from random import randint

def sample():
    print("""5 5
1 2 3 4 5
2 1 5
2 4 4
1 4 3
1 2 3
2 2 4""")

def brute():
    n = 5
    print(n, n * (n + 1) // 2)
    print(' '.join(str(x + 1) for x in range(n)))
    for i in range(n):
        for j in range(i, n):
            print(2, i + 1, j + 1)

def get_num(n):
    nums = list(filter(lambda x: x < n, [12, 18, 24, 60, 120, 2520, 55440]))
    return nums[randint(0, len(nums) - 1)] * randint(1, n // nums[-1])

def random(n):
    q = randint(1, n)
    print(n, q)
    arr = [get_num(n) for _ in range(n)]
    print(' '.join(str(x) for x in arr))
    for _ in range(q):
        t = randint(1, 2)
        if t == 1:
            i = randint(1, n)
            x = get_num(n)
            print(t, i, x)
        else:
            l = randint(1, n - 5)
            r = randint(l + 1, n)
            print(t, l, r)

def main():
    print(5)
    sample()
    brute()
    random(100)
    random(1000)
    random(10000)

main()
