from collections import deque  
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q, res = deque([]), []
        for i in range(len(nums)):

            # Don't pop anything on first window
            if (i >= k) and (q[0] == (i - k)):
                q.popleft()

            # Monotonic decreasing queue
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

            # Don't add to res until end of first window
            if i >= (k - 1):
                res.append(nums[q[0]])
                
        return res