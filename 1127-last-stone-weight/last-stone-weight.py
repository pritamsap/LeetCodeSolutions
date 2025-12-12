import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # convert current list to a maxHeap
        maxHeap = []
        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])


        while len(maxHeap) > 1:

            # first element pop
            x = -heapq.heappop(maxHeap)
            # second element pop
            y = -heapq.heappop(maxHeap)

            if x > y:
                z = x - y
                heapq.heappush(maxHeap, -z)
            # if they both equal don't do anything
        
 
        return -maxHeap[0] if len(maxHeap) == 1 else 0
                

        