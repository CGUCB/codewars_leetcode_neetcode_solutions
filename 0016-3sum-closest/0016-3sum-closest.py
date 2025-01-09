class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        d, r, nums, N = float('inf'), float('inf'), sorted(nums), len(nums)
        for i in range(N):
            nt = target - nums[i]
            j, k = i + 1, N - 1
            while j < k:
                cj, ck = nums[j], nums[k]
                nd = cj + ck - nt
                if abs(nd) < d:
                    r, d = nd + target, abs(nd)
                if cj + ck > nt:
                    k -= 1
                else:
                    j += 1
        return r
