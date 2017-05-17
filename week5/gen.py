import random

def sample():
    print("""7 9
1 2
2 3
3 4
4 2
4 5
2 5
5 6
5 7
4 6""")


def linked_list(n):
    print(n, n - 1)
    nodes = list(range(1, n + 1))
    random.shuffle(nodes)
    for i in range(1, n):
        print(nodes[i - 1], nodes[i])


def good_square():
    print("""4 5
1 2
1 3
1 4
2 3
3 4""")


def bad_square():
    print("""4 6
1 2
1 3
1 4
2 3
2 4
3 4""")

def disconnected():
    print("""4 2
1 2
3 4""")

def main():
    print(1 + 1 + 1 + 1 + 1 + 1)
    sample() # 1
    linked_list(10) # 1
    linked_list(500) # 1
    good_square() # 1
    bad_square() # 1
    disconnected() # 1

main()
