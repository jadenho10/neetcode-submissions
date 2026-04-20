class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = dict()
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            #update end 
            size += 1
            if lastIndex[c] > end:
                end = lastIndex[c]
            
            if end == i:
                res.append(size)
                size = 0
        return res
           