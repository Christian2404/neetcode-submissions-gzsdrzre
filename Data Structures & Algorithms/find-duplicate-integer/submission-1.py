class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # We can use the nums array as a seen set, where the index corrosponds to the value of the elem
        # We mark elem as seen by making it negative (nums are all positive)

        # For example in the arr [4,2,3,-1,4], for the first elem 4, we mark index 3 as being negative to indicate we have seen 4
        # If a elems absolute index position is already negative that is the duplicate position 

        for i, num in enumerate(nums):

            position = abs(num) - 1

            if nums[position] <= 0:
                return abs(num)
            else:
                nums[position] *= -1

        