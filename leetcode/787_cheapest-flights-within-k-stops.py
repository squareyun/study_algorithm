class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        prices = [float('inf')] * n
        prices[src] = 0
        
        for _ in range(k+1):
            prices_copy = prices[:]
            
            for source, target, price in flights:
                if prices_copy[source] != float('inf') and prices[source] + price < prices_copy[target]:
                    prices_copy[target] = prices[source] + price
            prices = prices_copy
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]
