class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Iterate through the array of intergers and tally up the total product and keep a zeros counter

        product = 1
        zeros_index = []

        for i, num in enumerate(nums): 
            if num != 0:
                product *= num
            else: 
                zeros_index.append(i)

        # Two or more zeros in the array, all elements will be zero 

        if len(zeros_index) >= 2:
            return [0] * len(nums)

        # One zero in the array means all elements except location of zero, will be zero

        if len(zeros_index) == 1:
            res = [0] * len(nums)
            res[zeros_index[0]] = product
            return res

        # Otherwise, return array of product * current element**-1

        res = []

        for i in range(len(nums)):
            res.append(int(product * nums[i]**-1))

        return res