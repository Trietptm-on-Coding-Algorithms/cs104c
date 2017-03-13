import random

random.seed(0x12)

# output 3, 1, -1
def sample():
    print("""2 28
1 0 3
5 5
1 1 1 1 1 0
1 0
1 3""")

# 4 2s
def pow2():
    for exp in range(31, 35):
        n = exp
        y = (1 << exp) + 1

        print(n, y)
        coeffs = ['1'] + ['0'] * (n - 1) + ['1']
        print(' '.join(coeffs))

# 5 ns
def pown():
    for exp in range(11, 16):
        n = exp
        ans = exp - 7
        y = (ans**exp) + 1

        print(n, y)
        coeffs = ['1'] + ['0'] * (n - 1) + ['1']
        print(' '.join(coeffs))

# 1e9 + 7
def linear():
    ans = int(1e9 + 7)
    c1, c0 = 10, 10
    n, y = 1, c1 * ans + c0
    print(n, y)
    print('{} {}'.format(c0, c1))

def not_exist():
    n, y = 10, int(1e9 + 7)

    print(n, y)
    print(' '.join(['2'] * (n + 1)))

# 0
def zero():
    n, y = 1000, 0
    print(n, y)
    coeffs = [0] + [random.randint(1, 1000) for _ in range(n)]
    print(' '.join(map(str, coeffs)))


# 1
def unit():
    n, y = 100000, 100001
    print(n, y)
    print(' '.join(['1'] * (n + 1)))

def main():
    T = 3 + 4 + 5 + 1 + 1 + 1 + 1
    print(T)
    sample()
    pow2()
    pown()
    linear()
    not_exist()
    zero()
    unit()

main()
