from collections import deque

def dfs(graph):
    hit = [0] * len(graph)
    q = deque()
    q.append(1)

    while q:
        node = q.popleft()
        hit[node] += 1

        for v in graph[node]:
            if hit[v] == 0:
                q.append(v)

    return hit

def get_degrees(nodes, graph):
    degree = [0] * (nodes + 1)

    for u in range(nodes + 1):
        for v in graph[u]:
            degree[u] += 1
            degree[v] += 1

    degree = [x // 2 for x in degree]
    return degree

ans = []
def find_tour(graph, node):
    while graph[node]:
        v = graph[node].pop()
        graph[v].remove(node)
        find_tour(graph, v)

    ans.append(node)

def main():
    nodes, edges = map(int, input().split())
    graph = [list() for _ in range(nodes + 1)]

    degree = [0] * (nodes + 1)
    for _ in range(edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

        degree[u] += 1
        degree[v] += 1

    hits = dfs(graph)

    connected = all(hits[u] > 0 for u in range(1, nodes + 1) if len(graph[nodes]) > 0)
    degrees = get_degrees(nodes, graph)
    odd_count = sum(1 for x in degrees if x % 2 == 1)

    if not connected or (odd_count not in (0, 2)):
        print(-1)
        return

    if odd_count == 0:
        start = 1
    else:
        for i in range(1, nodes + 1):
            if degrees[i] % 2 == 1:
                start = i
                break

    global ans
    ans = []
    find_tour(graph, start)
    print(' '.join(str(x) for x in ans))

T = int(input())
for _ in range(T):
    main()
