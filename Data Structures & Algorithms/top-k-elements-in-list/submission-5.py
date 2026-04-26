'''
use Counter to get freq of items

use array: index will represent count, elements will be inside of said count
need to have 0 to len(nums): index

quickselect algorithm

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        freqList = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            freqList[freq].append(num)
        
        res = []
        for i in range(len(freqList) - 1, -1, -1):
            for num in freqList[i]:
                res.append(num)
                if len(res) == k:
                    return res


