import pandas as pd 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        df = pd.DataFrame(data = nums, columns = ['value'] , dtype = int)
        df = df.dropna()
        print(df)
        if len(df) > k:
            maxs = df.rolling(window=k).max()
            maxs = maxs.dropna()
        else:
            max_ = df['value'].max()
            return [max_]
        print(maxs)
        return maxs['value'].astype(int).tolist()
        