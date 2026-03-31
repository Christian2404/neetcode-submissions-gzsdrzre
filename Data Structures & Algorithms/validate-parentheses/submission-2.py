class Solution:
    def isValid(self, s: str) -> bool:

        # Edge cases 
        
        if len(s) == 0:
            return False

        # Define data structs

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = [] 

        for c in s: 

        # if opening bracket (,[,{ append to stack
            if c not in brackets:
                stack.append(c)

            # If closing bracker },],) the top of stack should be corrosponding opening bracket 
            # if its not return false
            elif len(stack) > 0:
                stack_top = stack.pop() 

                if brackets[c] != stack_top:
                    return False

            else:
                return False
        return (len(stack) == 0)

