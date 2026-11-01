
def dfs(a, b, target, visited, path):
    if (a, b) in visited:
        return False

    visited.add((a, b))
    path.append((a, b))

    if a == target or b == target:
        return True

    moves = [
        (0, b), (a, 0),       # Empty a jug or b jug
        (a, b),                # Fill operations handled below
        (min(a_cap, a + b), max(0, a + b - b_cap)),
        (max(0, a + b - a_cap), min(b_cap, a + b)),
    ]

    # Generate all valid next states
    next_states = [
        (a_cap, b), (a, b_cap),  # Fill either jug
        (0, b), (a, 0),          # Empty either jug
        (a - min(a, b_cap - b), b + min(a, b_cap - b)),
        (a + min(b, a_cap - a), b - min(b, a_cap - a))
    ]

    for x, y in next_states:
        if dfs(x, y, target, visited, path):
            return True

    path.pop()
    return False


a_cap = int(input("Enter capacity of Jug A: "))
b_cap = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

visited = set()
path = []

if dfs(0, 0, target, visited, path):
    print("Solution path:")
    for state in path:
        print(state)
else:
    print("No solution found")
