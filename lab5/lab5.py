import matplotlib.pyplot as plt
import numpy as np


points = [(1, 1), (1, 2), (4, 1), (4, 4), (2, 2), (3, 1), (5, 4), (5, 5), (2, 3), (3, 5), (4.5, 2)]


def sOr(p1, p2, p3):
    return p2[0]*p3[1] - p3[0]*p2[1] - p1[0]*p3[1] + p3[0]*p1[1] + p1[0]*p2[1] - p2[0]*p1[1]


def dist(p1, p2, p3):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    return np.abs(np.cross(p2-p1, p1-p3) / np.linalg.norm(p2-p1))


def quick_hull(S, l, r):
    if len(S) == 0:
        return []
    h = S[0]
    for point in S:
        if np.any(dist(l, r, point) > dist(l, r, h)):
            h = point
    plt.plot([l[0], h[0]], [l[1], h[1]], 'y')
    plt.plot([r[0], h[0]], [r[1], h[1]], 'y')
    plt.plot([l[0], r[0]], [l[1], r[1]], 'y')
    S1 = []
    S2 = []
    for point in S:
        if sOr(l, h, point) < 0:
            S1.append(point)
        if sOr(h, r, point) < 0:
            S2.append(point)
    return quick_hull(S1, l, h) + [h] + quick_hull(S2, h, r)


def leftMost(S):
    candidate = S[0]
    for i in range(len(S)):
        if candidate[0] > S[i][0]:
            candidate = S[i]
    return candidate


def rightMost(S):
    candidate = S[0]
    for i in range(len(S)):
        if candidate[0] < S[i][0]:
            candidate = S[i]
    return candidate


def hull(S):
    l0 = leftMost(S)
    r0 = rightMost(S)
    S.remove(l0)
    S.remove(r0)
    S1 = []
    S2 = []
    for point in S:
        if sOr(l0, r0, point) < 0:
            S1.append(point)
        if sOr(l0, r0, point) > 0:
            S2.append(point)
    return [l0] + quick_hull(S1, l0, r0) + [r0] + quick_hull(S2, r0, l0) + [l0]


def draw():
    plt.plot(*zip(*points), 'og')
    res = hull(points)
    plt.plot(*zip(*res), 'r')
    plt.show()


draw()
