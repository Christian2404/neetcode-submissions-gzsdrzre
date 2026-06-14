class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Complement stores the: complement: index 
        # Loop through nums, first check if complement is in the map, then add itself to map & continue

        # Input: nums = [4,5,6]
        # target = 10
        # complement_map = {6: 0, 5: 1,}
        # i = 2, num = 6, target = 10

        complement_map = {}
        
        for i, num in enumerate(nums):
            
            if num in complement_map:
                return [complement_map[num], i]
            
            complement_map[target - num] = i
        

        