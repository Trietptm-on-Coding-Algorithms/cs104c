from collections import deque

def findCC(nodes, edges, start, maxlen):
    graph = [[]]
    for _ in range(nodes):
        graph.append([])
    for _ in range(edges):
        a, b = tuple(map(int, input().rstrip().split()))
        graph[a].append(b)
        graph[b].append(a)
    seen = set()
    cc = 0
    for node in range(1, nodes+1):
        q = deque()
        if node not in seen:
            cc += 1
            q.append(node)
            while len(q) > 0:
                cur = q.popleft()
                seen.add(cur)
                for to in graph[cur]:
                    if to not in seen:
                        q.append(to)
    seen = set()
    q = deque()
    q.append((start, 0))
    while len(q) > 0:
        cur, path = q.popleft()
        seen.add(cur)
        if path < maxlen:
            for to in graph[cur]:
                if to not in seen:
                    q.append((to, path+1))
    print(cc, len(seen))


def main():
    tests = int(input().rstrip())
    for _ in range(tests):
        nodes, edges, start, maxlen = tuple(map(int, input().rstrip().split()))
        findCC(nodes, edges, start, maxlen)

if __name__ == '__main__':
    main()
