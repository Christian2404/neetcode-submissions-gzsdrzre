class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0
        r = len(nums) - 1
        
        while l < r: # Find pivot (aka smallest value)

            middle = (l + r) // 2

            if nums[r] > nums[middle]: # right side is sorted so smallest val must be from l -> middle
                r = middle
            else: # Right side is unsorted meaning pivot must be in right side 
                l = middle + 1

        pivot = l # We can find the sub-array to perform b-search in 

        nums = nums[pivot:] + nums[:pivot] # Sort arr

        print(nums, pivot)
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            middle = (l + r) // 2

            if nums[middle] == target:
                return (middle + pivot) % len(nums) 
            elif nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1

        return -1


