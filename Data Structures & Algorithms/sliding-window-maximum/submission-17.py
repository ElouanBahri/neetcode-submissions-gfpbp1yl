from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Stores indices
        
        for i, val in enumerate(nums):
            # 1. Remove indices of elements smaller than current val from the back
            while q and nums[q[-1]] <= val:
                q.pop()
            
            q.append(i)
            
            # 2. Remove index from the front if it's out of window bounds
            if q[0] == i - k:
                q.popleft()
            
            # 3. Once we have a full window, the front is our max
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res