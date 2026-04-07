class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #--- APPROACH ---# 

        # Find the row, binary search the rows and check the range of values

        # Binary search the row for target 


        # --- TEST RUN --- #

        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        # target = 10
        # l = 0
        # r = 2
        # middle = 1 
        # row_index = 1 


        l = 0
        r = len(matrix) - 1
        row_index = None 

        while l <=r: 
            middle = (l + r) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row_index = middle
                break
            elif matrix[middle][0] >= target <= matrix[middle][-1]: # Target in left side 
                r = middle - 1
            elif matrix[middle][0] <= target >= matrix[middle][-1]: # Target in right side
                l = middle + 1

        if row_index is None: # Exists in space between rows 
            return False

        # Find the elem 
        row = matrix[row_index]

        # Row = [10,11,12,13]
        # l = 0
        # r = 0
        # middle = 0

        l = 0
        r = len(row) - 1

        while l <= r: 
            middle = (l + r) // 2

            if row[middle] == target:
                return True
            elif row[middle] < target:
                l = middle + 1
            elif row[middle] > target:
                r = middle - 1

        return False

