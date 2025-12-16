class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)
        nums.sort()
        def dfs(i, curr):
            if i >= n:
                res.append(curr[:])
                return
            

            # decision 1
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()

            # check duplicate and decision 2
            while i < len(nums) -1 and nums[i+1] == nums[i]:
                i += 1
            dfs(i + 1, curr)
        
        dfs(0, [])
        return res
        