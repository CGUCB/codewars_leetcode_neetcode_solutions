class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        r, N1, N2 = 0, len(nums1), len(nums2)
        if N2 % 2:
            while nums1:
                r = r ^ nums1.pop(0)
        if N1 % 2:
            while nums2:
                r = r ^ nums2.pop(0)
        return r