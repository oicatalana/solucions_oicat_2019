import random
import sys

class Tree:
    def __init__(self, height, value):
        self.m_left = None
        self.m_right = None
        self.m_height = height
        self.m_value = value
        self.m_max_value = value
        self.m_random = random.random()

def Update(tree):
    tree.m_max_value = tree.m_value
    if tree.m_left is not None:
        tree.m_max_value = max(tree.m_max_value, tree.m_left.m_max_value)
    if tree.m_right is not None:
        tree.m_max_value = max(tree.m_max_value, tree.m_right.m_max_value)

def Merge(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    if tree1.m_random >= tree2.m_random:
        tree1.m_right = Merge(tree1.m_right, tree2)
        Update(tree1)
        return tree1

    tree2.m_left = Merge(tree1, tree2.m_left)
    Update(tree2)
    return tree2

def Split(tree, x):
    if tree is None:
        return None, None
    if tree.m_height <= x:
        first, second = Split(tree.m_right, x)
        tree.m_right = first
        Update(tree)
        return tree, second

    first, second = Split(tree.m_left, x)
    tree.m_left = second
    Update(tree)
    return first, tree


for line in sys.stdin:
    v = [x for x in map(int, line.split(" "))][1:]
    n = len(v)

    tree = None
    result = 0
    for i in range(n):
        tree1, tree2 = Split(tree, v[i])
        value = v[i] if tree1 is None else v[i] + tree1.m_max_value
        tree = Merge(Merge(tree1, Tree(v[i], value)), tree2)
        result = max(result, value)

    print(result)
