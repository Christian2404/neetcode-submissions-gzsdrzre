class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Create a prefix array, where backtrack(n) =
        # element n contains the product from 0 ... n - 1

        n = len(nums)
        prefix_array = [1] * n

        for i in range(1, n):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]

        # Create a suffix array, where backtrack(n) =
        # element n contains the product from 0 ... n - 1
        
        suffix_array = [1] * n

        for i in range(n - 2, -1, -1):
            suffix_array[i] = suffix_array[i + 1] * nums[i + 1]
        
        # create a res array where it is the product of 
        # prefix and postfix

        res = [0] * n

        for i in range(n):
            res[i] = prefix_array[i] * suffix_array[i]

        return res