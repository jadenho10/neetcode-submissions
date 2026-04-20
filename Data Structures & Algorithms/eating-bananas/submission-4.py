'''
we can definitely eat at max(piles) speed
4 bananas per hour 

'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
