class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # two global list 
        res = []
        sol = []

        n = len(nums)

        # define a backtrack function 
        def backtrack(i):
            # if are done with the list
            if i == n:
                res.append(sol[:])
                return
            
            # dont pick the number
            backtrack(i + 1)

            # pick the number
            sol.append(nums[i])
            backtrack(i + 1)
            # it will pop one by one 
            sol.pop()
        
        backtrack(0)  
        return res



        