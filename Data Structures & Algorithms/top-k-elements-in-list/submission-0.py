class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for key, value in counter.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
            


            
        