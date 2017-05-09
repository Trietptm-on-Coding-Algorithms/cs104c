#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 200005;
int n;
int a[MAXN];
int tree[2 * MAXN];

int gcd(const int& a, const int& b) {
    if (a == 0) return b;
    return b == 0 ? a : gcd(b, a % b);
}

void build_tree() {
    memset(tree, 0, sizeof(tree));
    for (int i = 0; i < n; ++i) {
        tree[i + n] = a[i];
    }

    for (int i = n - 1; i > 0; --i) {
        tree[i] = gcd(tree[2 * i], tree[2 * i + 1]);
    }
}

void update(int i, int x) {
    int idx = i + n;
    tree[idx] = x;

    while (idx > 1) {
        idx /= 2;
        tree[idx] = gcd(tree[2 * idx], tree[2 * idx + 1]);
    }
}

int query(int l, int r) {
    int left = 0;
    int right = 0;

    for (int i = l + n, j = r + n; i <= j; i /= 2, j /= 2) {
        if ((i & 1) == 1)
            left = gcd(left, tree[i++]);
        if ((j & 1) == 0)
            right = gcd(tree[j--], right);
    }

    return gcd(left, right);
}

int main() {
    int T;
    scanf("%d", &T);

    int q;
    while (T-- > 0) {
        scanf("%d %d", &n, &q);

        for (int i = 0; i < n; ++i) {
            scanf("%d", a + i);
        }

        build_tree();

        int id, l, r;
        while (q-- > 0) {
            scanf("%d %d %d", &id, &l, &r);
            --l;

            if (id == 1) {
                update(l, r);
            } else {
                --r;
                printf("%d ", query(l, r));
            }
        }
        printf("\n");
    }

    return 0;
}
