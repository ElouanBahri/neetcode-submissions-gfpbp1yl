import heapq

class MedianFinder:
    def __init__(self):
        # small_h is a max-heap (stores the smaller half)
        # large_h is a min-heap (stores the larger half)
        self.small_h = [] 
        self.large_h = []

    def addNum(self, num: int) -> None:
        # 1. Push to max-heap (small_h), then move the largest of those to min-heap (large_h)
        heapq.heappush(self.small_h, -num)
        heapq.heappush(self.large_h, -heapq.heappop(self.small_h))
        
        # 2. Rebalance: small_h can have at most 1 more element than large_h
        if len(self.large_h) > len(self.small_h):
            heapq.heappush(self.small_h, -heapq.heappop(self.large_h))

    def findMedian(self) -> float:
        if len(self.small_h) > len(self.large_h):
            return float(-self.small_h[0])
        return (-self.small_h[0] + self.large_h[0]) / 2.0