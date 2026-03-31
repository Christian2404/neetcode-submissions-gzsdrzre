class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # nums=[2,20,4,10,3,4,5]
        
        # If nums is empty return 0

        if len(nums) == 0:
            return 0

        # Create a bucket with negative bias
        # so bucket[i] = min element
        # len(bucket) = range min(nums) -> max(nums)

        lower = min(nums)
        upper = max(nums)
        n = upper - lower

        bucket = [0] * (n + 1)

        # bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # The bias value is equal to the lower bound

        # If lower = 13, bias will be 13 meaning that bucket[0] maps to 13

        # if lower = -5, bias is negative 5 meaning that bucket[0] maps to negative 5

        for num in nums:
            bucket[num - lower] = 1  

        # Iterate through bucket count maximum consecutive 

        counter = 0
        max_counter = 0

        for val in bucket:

            if val == 1:
                counter += 1
            else:
                max_counter = max(counter, max_counter)
                counter = 0

        # Return max

        return max(counter, max_counter)