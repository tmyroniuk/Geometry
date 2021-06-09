import matplotlib.pyplot as plt

points = [(0, 0), (1, 1), (1, 2), (4, 1), (4, 4), (2, 2), (3, 1), (5, 4), (5, 5), (2, 3), (3, 5), (3, 2), (3.5, 2.5), (4.5, 2)]


def sOr(p1, p2, p3):
    return p2[0]*p3[1] - p3[0]*p2[1] - p1[0]*p3[1] + p3[0]*p1[1] + p1[0]*p2[1] - p2[0]*p1[1]


def findNextPointIndex(prevIndex):
    candidate = prevIndex + 1
    if candidate == len(points):
        candidate = 0
    for i in range(len(points)):
        if (i != prevIndex) & (i != candidate) & (sOr(points[prevIndex], points[candidate], points[i]) <= 0):
            candidate = i
    return candidate


def leftMost():
    candidate = 0
    for i in range(len(points)):
        if points[i][0] < points[candidate][0]:
            candidate = i
    return candidate


def Jarvis(S):
    res = [leftMost()]
    while (len(res) == 1) | (res[len(res) - 1] != res[0]):
        res.append(findNextPointIndex(res[len(res) - 1]))
        plt.plot([S[res[len(res) - 1]][0],  S[res[len(res) - 2]][0]], [S[res[len(res) - 1]][1],  points[res[len(res) - 2]][1]], 'r')


def draw(S):
    plt.plot(*zip(*S), 'o')
    Jarvis(S)
    plt.show()


draw(points)
