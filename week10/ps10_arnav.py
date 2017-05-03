import functools

def compare(a, b):
    if a[0][0] == b[0][0]:
        return a[0][1] - b[0][1]
    return a[0][0] - b[0][0]


def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def compute_hull(points):
    hull = []
    # Top half and bottom half
    for _ in range(2):
        start_size = len(hull)
        for point in points:
            while len(hull) >= start_size + 2 \
                    and ccw(hull[-2][0], hull[-1][0], point[0]) <= 0:
                hull.pop()

            hull.append(point)

        hull.pop()

        points = reversed(list(points))

    return hull


def main():
    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        points = []
        for i in range(n):
            x, y = map(int, input().split())
            points.append(((x, y), i))

        points.sort(key=functools.cmp_to_key(compare))

        hull = compute_hull(points)
        indexes = [index for point, index in hull]
        indexes.sort()

        print(' '.join(str(index) for index in indexes))


main()
