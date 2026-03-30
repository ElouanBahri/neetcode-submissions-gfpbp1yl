class Solution:

    def IsAnagram(self, str1: str, str2: str):
        d1 = {}
        d2 = {}
        for l in str1:
            if l in d1.keys():
                d1[l] += 1
            else :
                d1[l] = 1 
        for l in str2:
            if l in d2.keys():
                d2[l] += 1
            else :
                d2[l] = 1
        print(d1 == d2)
        return d1 == d2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        d = {0 : [strs[0]]}
        i = 0
        for k in strs[1:] :
            find = False 
            print(k)
            for keys in d.keys():
                if self.IsAnagram(k,d[keys][0]) :
                    d[keys] += [k]
                    find = True 
                    continue
            if not find:
                i += 1
                print(k)
                d[i] = [k]
        for keys in d.keys():
            result += [d[keys]]
        
        return result




        