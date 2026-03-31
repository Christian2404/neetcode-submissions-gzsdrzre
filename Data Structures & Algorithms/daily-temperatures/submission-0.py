class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures) # [1, 4, 1, 2, 1, 0, 0]
        stack = [len(temperatures) - 1] # [5, 1]

        # temperatures = [30,38,30,36,35,40,28]

        # We need to make sure that stack is in decreasing order from bottom to top
        curr_index = len(temperatures) - 2 # 0

        while stack and curr_index >= 0:

            if temperatures[curr_index] < temperatures[stack[-1]]: # Next largest day
                res[curr_index] = stack[-1] - curr_index # Number of days
                stack.append(curr_index)
                curr_index -= 1 # Look at next elem

            else:
                stack.pop()
                if not stack: # No elements greater
                    stack.append(curr_index)
                    curr_index -= 1
            

        return res 
