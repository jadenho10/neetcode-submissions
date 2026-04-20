class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, price in flights:
                if prices[s] != float('inf') and prices[s] + price < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + price
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]
            
