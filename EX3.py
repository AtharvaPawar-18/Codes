
from collections import deque

def solve(n):
    start = (0,) * n
    goal = (2,) * n
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            for move in path:
                print(move)
            print("Total moves:", len(path))
            return

        pegs = [[], [], []]

        for disk, peg in enumerate(state):
            pegs[peg].append(disk)

        for a in range(3):
            if not pegs[a]:
                continue

            disk = pegs[a][0]

            for b in range(3):
                if a == b:
                    continue

                if not pegs[b] or pegs[b][0] > disk:
                    new = list(state)
                    new[disk] = b
                    new = tuple(new)

                    if new not in visited:
                        visited.add(new)
                        move = f"Move disk {disk+1} from {a} to {b}"
                        q.append((new, path + [move]))

n = int(input("Enter number of disks: "))
solve(n)
