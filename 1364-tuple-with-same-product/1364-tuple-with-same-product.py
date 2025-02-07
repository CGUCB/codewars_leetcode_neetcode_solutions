from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            for y in nums[i + 1:]:
                if x != y:
                    d[x * y].append([x, y])
        
        total = 0
        for v in d.values():
            l = len(v)
            if l >= 2:
                total += (l * 2) * ((l - 1) * 2)
        
        return total

