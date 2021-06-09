import matplotlib.pyplot as plt


points = [(1, 1), (2, 4), (2, 5), (2, 7), (3, 6), (4, 2), (4, 4), (5, 3)]
region = [(0, 0), (2, 0), (2, 2), (0, 2)]


class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __repr__(self):
        return str(self.begin) + " --> " + str(self.end)


class Node:
    def __init__(self, interval, left_son, right_son):
        self.interval = interval
        self.left_son = left_son
        self.right_son = right_son
        self.in_intervals = []

    def __repr__(self):
        return "{" + str(self.interval) + " l:" + str(self.left_son) + " r:" + str(self.right_son) + str(
            self.in_intervals) + "}"


def insert(root, i):
    if root is None:
        return Node(i, None, None)

    b = root.interval.begin
    e = root.interval.end
    if i.begin[0] <= b[0] and i.end[0] >= e[0]:
        root.in_intervals.append(i)
    if i.begin[0] <= (e[0] + b[0]) / 2:
        root.left_son = insert(root.left_son, i)
    if i.end[0] > (e[0] + b[0]) / 2:
        root.right_son = insert(root.right_son, i)
    return root


def make_intervals(array):
    result = []
    size = len(array)
    for i in range(size - 1):
        new_interval = Interval(array[i], array[i + 1])
        result.append(new_interval)
    return result


def inorder(root):
    if root is None:
        return

    inorder(root.left_son)
    nodes.append(root)
    inorder(root.right_son)


n = len(points)

intervals = make_intervals(points)

tree_root = Node(Interval(points[0], points[n - 1]), None, None)
# tree_root = None
for i in range(0, len(intervals)):
    tree_root = insert(tree_root, intervals[i])

region_interval = Interval(region[0], region[2])
tree_root = insert(tree_root, region_interval)

nodes = []
nodes_for_region = []
inorder(tree_root)
for i in range(0, len(nodes)):
    if region_interval in nodes[i].in_intervals:
        nodes_for_region.append(nodes[i])

result = []
for node in nodes_for_region:
    b = node.interval.begin
    e = node.interval.end
    if b[1] > region_interval.end[1] or b[1] < region_interval.begin[1]:
        continue
    else:
        if b not in result:
            result.append(b)
    if e[1] > region_interval.end[1] or e[1] < region_interval.begin[1]:
        continue
    else:
        if e not in result:
            result.append(e)

plt.plot(*zip(*points), 'ro')
plt.plot(*zip(*region), 'g')
plt.plot([region[0][0], region[len(region)-1][0]], [region[0][1], region[len(region)-1][1]], 'g')
plt.show()
