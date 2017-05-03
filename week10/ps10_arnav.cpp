/*
USER: rednano1
PROG: fc
LANG: C++11
*/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <complex>
#include <algorithm>
#include <cmath>
#include <vector>
#include <utility>

using namespace std;

// A simple point
typedef pair<int, int> pt;

// A point with an index
typedef pair<pt, int> pt_index;

int n;

vector<pt> points;
vector<pt> convex_hull;

bool cmp(pt& a, pt& b) {
    if (a.first == b.first) {
        return a.second < b.second;
    }

    return a.first < b.first;
}

double dist(pt a, pt b) {
    double x = a.first - b.first;
    double y = a.second - b.second;
    return sqrt(x * x + y * y);
}

/*
 *  i j k
 *  a b 0
 *  c d 0
 */

double ccw(pt a, pt b, pt c) {
    return (b.first - a.first) * (c.second - a.second) - (b.second - a.second) * (c.first - a.first);
}

void compute_hull() {
    convex_hull.clear();

    for (int step = 0; step < 2; ++step) {
        size_t start = convex_hull.size();

        for (pt p : points) {
            while (convex_hull.size() >= start + 2
                    and ccw(convex_hull[convex_hull.size() - 2], convex_hull[convex_hull.size() - 1], p) <= 0) {
                convex_hull.pop_back();
            }

            convex_hull.push_back(p);
        }

        convex_hull.pop_back();
        reverse(points.begin(), points.end());
    }
}

int main() {
    cin >> n;
    int x, y;
    for (int i = 0; i < n; ++i) {
        cin >> x >> y;
        points.push_back(pt(x, y));
    }

    // find the smallest point
    sort(points.begin(), points.end(), cmp);

    compute_hull();

    if (sz > 2)
        ans += dist(convex_hull[sz - 1], convex_hull[0]);

    fout << fixed << setprecision(2) << ans << '\n';
    fout.close();

    return 0;
}
