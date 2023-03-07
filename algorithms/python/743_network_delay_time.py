from heapq import heappush, heappop

class Solution:
    weights = None

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        self.__generate_adj_list(times, n)
        
        return self.__djikstra(k)
    
    def __generate_adj_list(self, times: list[list[int]], n: int) -> None:
        weights = {i: set() for i in range(n)}

        for u, v, w in times:
            weights[u-1].add((v-1, w))
        self.weights = weights

    def __djikstra(self, start: int) -> int:
        min_heap = []
        min_heap.append((0, start-1))

        distance = [float('inf')] * len(self.weights)
        distance[start-1] = 0

        while min_heap:
            lowest_cost, node = heappop(min_heap)
            for neighbour, cost in self.weights[node]:
                if distance[neighbour] > distance[node] + cost:
                    distance[neighbour] = distance[node] + cost
                    heappush(min_heap, (distance[neighbour], neighbour))

        return max(distance) if max(distance) != float('inf') else -1
