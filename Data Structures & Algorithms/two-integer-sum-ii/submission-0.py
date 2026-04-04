class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Nums in increasing order 

        # Return [index1, index2] in increasing order 

        # Must use constant space 

        # solution: use two pointer, first pointer iterates by one element 
        # and we search for complement with binary search because the array is sorted

        # --- START --- # 

        for i, num in enumerate(numbers): 

            # numbers = [1,2,3,4] 
            # target = 3

            # l = 1
            # r = 1
            # complement = 2
            # middle_index = 1

            l = i + 1 
            r = len(numbers) - 1 
            complement = target - num 

            while l <= r: 

                middle_index = ((l + r) // 2) 

                # Is complement
                if numbers[middle_index] == complement:
                    return [i + 1, middle_index + 1]

                # Left sub-array
                elif numbers[middle_index] > complement:
                    r = middle_index - 1

                # Right sub-array 
                elif numbers[middle_index] < complement:
                    l = middle_index + 1

            





