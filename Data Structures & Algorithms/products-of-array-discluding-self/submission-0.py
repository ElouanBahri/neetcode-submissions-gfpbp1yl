class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            total = 1
            for j in nums[:i] + nums[i+1:]:
                total *= j
            result += [total]
        return result

            
        