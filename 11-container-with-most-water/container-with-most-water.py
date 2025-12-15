class Solution:
    def maxArea(self, height: List[int]) -> int:

        # given array with height
        # width is 1 point from each index in array
        # two pointer
        # l on index 0 and r on last index
        # return max water hold 
        # if height[l + 1] > height[r - 1]
        # [1,2,4,3]
        
        l = 0
        r = len(height) - 1
        maxWater = 0
        while l < r:
            minHeight = min(height[l], height[r])
            waterArea = (r - l) * minHeight
            maxWater = max(maxWater, waterArea)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxWater


