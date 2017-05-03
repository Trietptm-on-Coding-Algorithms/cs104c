import random

t = 40
print t

for q in range(t):
    n = random.randint(1, 1000)
    c = random.randint(1, 1000)
    print n, c
    for i in range(n):
        print random.randint(1, 10000), random.randint(1, 10000)
