import sys

input = sys.stdin.readline
tree = dict()
n = int(input())

for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]


def preorder(root):
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if node != ".":
            result.append(node)
            stack.append(tree[node][1])
            stack.append(tree[node][0])

    return "".join(result)


def inorder(root):
    stack = []
    result = []
    current = root

    while stack or current != ".":
        while current != ".":
            stack.append(current)
            current = tree[current][0]

        current = stack.pop()
        result.append(current)
        current = tree[current][1]

    return "".join(result)


def postorder(root):
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if node != ".":
            result.append(node)
            stack.append(tree[node][0])
            stack.append(tree[node][1])

    return "".join(result[::-1])


print(preorder("A"))
print(inorder("A"))
print(postorder("A"))
