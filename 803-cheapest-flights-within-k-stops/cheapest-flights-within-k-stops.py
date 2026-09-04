class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float('inf')
        
        price = [INF] * n
        price[src] = 0

        for _ in range(k + 1):
            temp = price.copy()

            for u, v, cost in flights:
                if price[u] != INF:
                    temp[v] = min(temp[v], price[u] + cost)

            price = temp

        return -1 if price[dst] == INF else price[dst]