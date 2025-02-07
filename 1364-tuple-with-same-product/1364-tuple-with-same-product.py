class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(lambda : 0)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                p = nums[i] * nums[j]
                d[p] += 1
        
        total = 0
        for v in d.values():
            if v >= 2:
                total += (v * 2) * ((v - 1) * 2)
        
        return total

