
from collections import deque

n = int(input("Enter grid size: "))

grid = []
print("Enter grid (0 = free, 1 = obstacle):")
for i in range(n):
    grid.append(list(map(int, input().split())))

sr, sc = map(int, input("Enter start (row col): ").split())
gr, gc = map(int, input("Enter goal (row col): ").split())

start = (sr, sc)
goal = (gr, gc)

q = deque([(start, [start])])
visited = {start}

while q:
    (r, c), path = q.popleft()

    if (r, c) == goal:
        print("Path:", path)
        print("Steps:", len(path) - 1)
        break

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < n and 0 <= nc < n and
            grid[nr][nc] == 0 and (nr, nc) not in visited):
            visited.add((nr, nc))
            q.append(((nr, nc), path + [(nr, nc)]))
else:
    print("No path found")
