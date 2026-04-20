class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # value : freq
        
        freqList = [[] for _ in range(len(nums) + 1)]

        for val, freq in count.items():
            freqList[freq].append(val)
        
        res = []
        for i in range(len(freqList) - 1, -1, -1):
            for num in freqList[i]:
                res.append(num)
                if len(res) == k:
                    return res