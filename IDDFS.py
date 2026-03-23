# Tree represented as adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Depth-Limited Search
def dls(node, target, depth, path):
    if depth < 0:
        return None

    path.append(node)

    if node == target:
        return path

    if depth == 0:
        path.pop()
        return None

    for child in tree[node]:
        result = dls(child, target, depth - 1, path)
        if result:
            return result

    path.pop()
    return None

# IDDFS
def iddfs(start, target, max_depth):
    for depth in range(max_depth + 1):
        path = []
        result = dls(start, target, depth, path)
        if result:
            return result
    return None


# Example
start_node = 1
target_node = 7
max_depth = 3

result = iddfs(start_node, target_node, max_depth)

if result:
    print("Path found:", " -> ".join(map(str, result)))
else:
    print("Target not found")