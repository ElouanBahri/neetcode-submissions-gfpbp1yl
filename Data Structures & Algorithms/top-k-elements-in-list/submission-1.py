class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        for i in range(0,k):
            max_key = max(d, key=d.get)
            d.pop(max_key)
            result += [max_key]
        return result