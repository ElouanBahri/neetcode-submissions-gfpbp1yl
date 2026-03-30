class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_ = {}
        d__ = {}
        for l in s : 
            if l in d_.keys() :
                d_[l] += 1
            else :
                d_[l] = 1 
        for l in t : 
            if l in d__.keys() :
                d__[l] += 1
            else :
                d__[l] = 1 
        return d_ == d__

        