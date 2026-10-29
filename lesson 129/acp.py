from collections import deque

def minDiceThrows(moves, N):
    visited = [False] * N

    q = deque()

    visited[0] = True
    q.append((0, 0))  # (cell, dice throws)

    while q:
        cell, dist = q.popleft()

        if cell == N - 1:
            return dist

        for dice in range(1, 7):
            nxt = cell + dice

            if nxt < N and not visited[nxt] == True:

                # If snake or ladder exists
                if moves[nxt] != -1:
                    q.append((moves[nxt], dist + 1))
                else:
                    q.append((nxt, dist + 1))

    return -1


# Example
N = 30
moves = [-1] * N

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print(minDiceThrows(moves, N))