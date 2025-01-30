from itertools import pairwise
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        M, N = len(isWater), len(isWater[0])
        q, grid = deque([]), [[-1] * N for _ in range(M)]

        # Add water to grid and queue
        for i in range(M):
            for j in range(N):
                if isWater[i][j]:
                    grid[i][j] = 0
                    q.append([i, j])
        
        # BFS on grid
        while q:
            i, j = q.popleft()
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if (0 <= x < M) and (0 <= y < N) and (grid[x][y] == -1):
                    grid[x][y] = grid[i][j] + 1
                    q.append([x, y])
        
        return grid