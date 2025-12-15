class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # array nums
        # return array answer, answer[i] is product of element num
        # except nums[i]
        # nums = [1,2,3,4]
        # output: [24,12,8,6]
        # prefix: [1, 1, 2, 6]
        # postfix: [24,12,4,1]

        # output: [24, 12, 8, 6]

        # first pass loop
        # calculating the prefix without nums[i] itself
        prefixArr = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefixArr[i] = prefix
            prefix = prefix * nums[i]
        
        # second pass, going reverse
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            prefixArr[j] = prefixArr[j] * postfix
            postfix = postfix * nums[j]
    
        return prefixArr



            

    
