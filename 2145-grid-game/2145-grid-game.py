class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N, r1, r2 = len(grid[0]), grid[0], grid[1]
        suf, pre = [r1[-1]] + [0] * (N - 1), [r2[0]] + [0] * (N - 1)

        # Prefix & Suffix Sum
        for i in range(1, N):
            suf[i] = suf[i - 1] + r1[-i - 1]
            pre[i] = pre[i - 1] + r2[i]
        suf = suf[::-1]

        r = float('inf')
        for i in range(N):
            s = 0 if i >= N - 1 else suf[i + 1]
            p = 0 if i < 1 else pre[i - 1]
            r = min([r, max([s, p])])

        return r
            