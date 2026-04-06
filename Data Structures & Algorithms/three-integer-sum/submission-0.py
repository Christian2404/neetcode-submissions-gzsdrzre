class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort the array, create three pointers: i, j, k.
        # For each elem i, pointers j and k will start at leftmost
        # and rightmost portion of the array respecively 
        # If the current sum < 0, move j to the right, if sum > 0
        # move k to the left, if == 0, append to res. 

        # nums = [-4, -1, -1, 0, 1, 2]
        # res = [[-1, -1, 2], [-1, 0, 1]]
        # i = 1
        # j = 3 
        # k = 4
        # sum = 1

        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2): 

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1


            while j < k: # When pointers overlap or meet there is no more solution 
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j += 1
                    sum = nums[i] + nums[j] + nums[k]
                elif sum > 0:
                    k -= 1
                    sum = nums[i] + nums[j] + nums[k]
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res 



