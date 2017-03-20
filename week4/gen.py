import random

num_possible = 3
num_finite = 4
num_not_possible = 3
num_tests = num_possible + num_finite + num_not_possible
max_nodes = 1000
max_edges = 1000
max_initial_health = 1000
min_edge_weight = -1000
max_edge_weight = 1000

def dedupe_edges(edges):
    ans = []
    used = set()
    for u, v, c in edges:
        if (u, v) in used:
            continue
        used.add((u, v))
        ans.append((u, v, c))
    return ans

def gen_random_possible_test():
    n = random.randint(20, max_nodes)
    m = random.randint(n - 1, min(n * (n - 1), max_edges))
    k = random.randint(0, max_initial_health)
    edges = []
    for i in range(n - 1):
        c = random.randint(min_edge_weight, max_edge_weight)
        edges.append((i + 1, i + 2, c))
    for i in range(m - n + 1):
        u = random.randint(1, n)
        v = random.randint(1, n)
        while u == v:
            v = random.randint(1, n)
        c = random.randint(min_edge_weight, max_edge_weight)
        edges.append((u, v, c))
    edges = dedupe_edges(edges)
    return n, len(edges), k, edges

def gen_random_finite_test():
    n = random.randint(20, max_nodes)
    m = random.randint(n - 1, min(n * (n - 1), max_edges))
    k = random.randint(0, max_initial_health)
    perm = range(2, n)
    random.shuffle(perm)
    perm = [1] + perm + [n]
    edges = []
    for i in range(n - 1):
        c = random.randint(min_edge_weight, max_edge_weight)
        edges.append((perm[i], perm[i + 1], c))
    for i in range(m - n + 1):
        u = random.randint(0, n - 2)
        v = random.randint(u + 1, n - 1)
        c = random.randint(min_edge_weight, max_edge_weight)
        edges.append((perm[u], perm[v], c))
    edges = dedupe_edges(edges)
    return n, len(edges), k, edges

def gen_random_not_possible_test():
    n = random.randint(20, max_nodes)
    m = random.randint(1, min(n * (n - 1), max_edges))
    k = random.randint(0, max_initial_health)
    perm = range(1, n)
    random.shuffle(perm)
    perm.append(n)
    edges = []
    for i in range(m):
        u = random.randint(0, n - 2)
        v = random.randint(u + 1, n - 1)
        c = random.randint(min_edge_weight, max_edge_weight)
        edges.append((perm[v], perm[u], c))
    edges = dedupe_edges(edges)
    return n, len(edges), k, edges

def test_to_string(test):
    n, m, k, edges = test
    return '%d %d %d\n%s' % (n, m, k, '\n'.join(map(lambda e: ' '.join(map(str,
        e)), edges)))

print num_tests
for i in range(num_possible):
    print test_to_string(gen_random_possible_test())
for i in range(num_finite):
    print test_to_string(gen_random_finite_test())
for i in range(num_not_possible):
    print test_to_string(gen_random_not_possible_test())
