class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #--- TEST RUN ---#

        # nums = [-1,0,2,4,6,8]
        # target = 4
        # l = 3
        # r = 3
        # middle = 4
        
        l = 0
        r = len(nums) - 1

        while r >= l:

            middle = r + l // 2 

            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target: 
                l = middle + 1
            else: 
                return middle

        return -1
                