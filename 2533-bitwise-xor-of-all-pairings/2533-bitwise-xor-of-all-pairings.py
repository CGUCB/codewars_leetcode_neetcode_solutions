class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        r, N1, N2 = 0, len(nums1), len(nums2)
        if N2 % 2:
            for n in nums1:
                r ^= n
        if N1 % 2:
            for n in nums2:
                r ^= n
        return r