
import heapq

# Calculate Manhattan Distance (Heuristic)
def h(s, goal):
    d = 0

    for i in range(9):
        if s[i] != 0:  # Ignore blank tile
            j = goal.index(s[i])

            # Calculate distance of each tile
            d += abs(i//3 - j//3) + abs(i%3 - j%3)

    return d


# A* Search Algorithm
def astar(start, goal):

    # Priority queue: (f, g, state, path)
    pq = [(h(start, goal), 0, start, [start])]
    visited = set()

    while pq:

        # Get state with minimum f value
        f, g, s, path = heapq.heappop(pq)

        # Check goal state
        if s == goal:
            return path

        if s in visited:
            continue

        visited.add(s)

        # Find blank tile position
        z = s.index(0)
        r, c = z//3, z%3

        # Possible movements: up, down, left, right
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:

            nr, nc = r+dr, c+dc

            # Check valid movement
            if 0 <= nr < 3 and 0 <= nc < 3:

                nz = nr*3 + nc

                # Swap blank tile with adjacent tile
                a = list(s)
                a[z], a[nz] = a[nz], a[z]
                ns = tuple(a)

                if ns not in visited:

                    ng = g + 1  # Actual cost
                    nf = ng + h(ns, goal)  # f = g + h

                    # Add new state to priority queue
                    heapq.heappush(pq, (nf, ng, ns, path+[ns]))

    return None


# Main Program: Take user input
start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))

# Validate input
if len(start) != 9 or len(goal) != 9 or set(start) != set(range(9)) or set(goal) != set(range(9)):
    print("Invalid input")

else:
    result = astar(start, goal)

    # Display solution
    if result:
        for s in result:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()

        print("Total Moves:", len(result)-1)

    else:
        print("No solution")
