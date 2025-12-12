class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n) - min Heap
        heapq.heapify(nums)

        # popping until len size k
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]





        
    
        