from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones) 

        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            if x < y:
                heappush(stones, x - y)

        stones.append(0)
        return abs(stones[0])

