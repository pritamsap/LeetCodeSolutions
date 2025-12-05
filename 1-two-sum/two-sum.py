class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            
            diff = target - v 

            if diff in hashmap: 
                return [i, hashmap[diff]]
            hashmap[v] = i
        
        


        
        