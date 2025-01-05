class Solution(object):
    def search(self, nums, target):

        # Base cases
        if not nums: 
            return -1
        
        a, b = 0, len(nums) - 1
        while a <= b:
            m = (a + b) // 2
            c = nums[m]

            if c == target:
                return m
            
            elif target > c:
                a = m + 1
            
            else:
                b = m - 1
        
        return -1

        