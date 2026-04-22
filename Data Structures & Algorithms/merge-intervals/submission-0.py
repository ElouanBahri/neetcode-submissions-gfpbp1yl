class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Edge case: if there's only 0 or 1 interval
        if not intervals:
            return []
        
        # 2. Sort by the start time - O(N log N)
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged is empty or no overlap, append the interval
            # No overlap if: current start > last merged end
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Overlap exists, merge by updating the end time
                # We take the max because the current interval could be 
                # entirely inside the previous one [[1, 10], [2, 5]]
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged