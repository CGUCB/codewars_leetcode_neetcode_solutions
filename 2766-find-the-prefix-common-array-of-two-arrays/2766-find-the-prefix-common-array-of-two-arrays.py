class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        f, r = set([]), [0 for _ in range(N)]
        for i in range(N):
            f.add(A[i])
            f.add(B[i])
            r[i] = (2 * (i + 1)) - len(f)
        return r