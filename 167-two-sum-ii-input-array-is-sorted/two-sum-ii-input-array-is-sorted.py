class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # array numbers integers are sorted
        # find two integer that sum to the target
        # return the two numbers index added by one
        # [2, 7, 11, 15] target = 9
        # could use HashMap but extra O(n) space
        # two pointer L and R
        # because we know it's sorted array the larger value will always be on the right
        # 2 + 15 = 17 > 9, shift R
        # 2 + 11 = 13 > 9, shift R
        # 2 + 7 = 9 = 9 found it

        l = 0
        r = len(numbers) - 1
        output = []
        for i in range(len(numbers)):
            if numbers[l] + numbers[r] == target:
                output.append(l + 1)
                output.append(r + 1)
                return output
            elif numbers[l] + numbers[r] > target:
                r  -= 1
            else:
                l += 1
        return output

        

        