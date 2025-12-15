class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left rotated array
        # ascending order
        # find the target
        # else return -1
        # binary search bit the rotated array is not sorted
        # two halves sorted and unsorted
        # [4, 5, 6, 7, 0, 1, 2]
        # [1, 2, 4, 5, 6, 7, 0]
        # [5, 6, 7, 0, 1, 2, 3]
        # 7 is the med 
        # [4 to 7] sorted, [m+1 to 2 is sorted]

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
        
            # check if left is sorted
            if nums[l] <= nums[mid]:
                # check if value is in left
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1 
                else:
                    l = mid + 1

            # if right is sorted
            else:
                # check if value is in right
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1 
                else:
                    r = mid - 1
        
        return -1


            

