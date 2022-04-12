class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<Node data={self.data}>"


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    nodes = map(int, f.readline().strip().split(' '))
    v = list(map(int, f.readline().strip().split(' ')))

    root = None
    for data in nodes:
        node = Node(data)

        if root is None:
            root = node
            continue

        def append(root, node):
            if node.data < root.data:
                if root.left:
                    append(root.left, node)
                else:
                    root.left = node
            if node.data > root.data:
                if root.right:
                    append(root.right, node)
                else:
                    root.right = node

        append(root, node)

    ancestors = []

    def traverse(node, stack):
        stack.append(node)

        if node.data in v:
            ancestors.append(stack.copy())

        if len(ancestors) == 2:
            return

        if node.left:
            traverse(node.left, stack)

        if node.right:
            traverse(node.right, stack)

        stack.pop()

    traverse(root, [])

    lca = None
    for v1, v2 in zip(ancestors[0], ancestors[1]):
        if v1.data != v2.data:
            break
        lca = v1.data

    print(lca)
