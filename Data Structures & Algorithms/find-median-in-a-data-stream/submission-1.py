import pandas as pd

class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr += [num]

    def findMedian(self) -> float:
        df  = pd.DataFrame(data = self.arr, columns = ['value'])
        return float(df['value'].median())
        
        