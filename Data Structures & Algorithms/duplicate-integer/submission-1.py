class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(0,len(nums)):
            if nums[i] in d.keys():
                return True
            else:
                d[nums[i]] = 1 
        return False
        