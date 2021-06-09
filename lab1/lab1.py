import matplotlib.pyplot as plt

points = [(1, 1), (2, 1), (2, 2), (1.5, 2.5), (1, 2.2), (0.5, 1.5)]
z = (1, 1.5)


def centroid():
    return (points[0][0] + points[1][0] + points[2][0]) / 3, (points[0][1] + points[1][1] + points[2][1]) / 3


def sOr(p1, p2, p3):
    return p2[0]*p3[1] - p3[0]*p2[1] - p1[0]*p3[1] + p3[0]*p1[1] + p1[0]*p2[1] - p2[0]*p1[1]


def test(S, q):
    for i in range(len(S) - 1):
        if (sOr(z, q, S[i+1]) <= 0) & (sOr(z, q, S[i]) >= 0):
            if sOr(S[i], S[i + 1], z) >= 0:
                return True
            else:
                return False


def draw():
    q = centroid()
    plt.plot(*q, 'oy')
    for point in points:
        plt.plot([q[0], point[0]], [q[1], point[1]], 'y-')
    points.append(points[0])
    plt.plot(*zip(*points), 'r-')
    plt.plot(*z, 'og', label=('Inside' if test(points, q) else 'Outside'))
    plt.legend()
    plt.show()


draw()
