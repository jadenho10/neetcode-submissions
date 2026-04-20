class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        count = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            count[freq].append(num)
        
        res = []
        for i in range(len(count) - 1, -1, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res