class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def countShips(cap):
            currCap = cap
            ships = 1
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships
              
        while l <= r:
            m = l + (r - l) // 2
            ships = countShips(m)
            if ships <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

        
