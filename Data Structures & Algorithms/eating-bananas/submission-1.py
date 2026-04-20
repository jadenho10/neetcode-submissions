class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles) # O(N)
        l = 1
        res = r

        while l <= r:
            time = 0
            mid = l + (r - l) // 2
            for p in piles:
                time += math.ceil(float(p) / mid)
            if time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


        
