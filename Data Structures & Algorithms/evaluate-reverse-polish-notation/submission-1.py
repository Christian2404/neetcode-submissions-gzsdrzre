class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '*', '/']
        operand_stack = []

        # Edge cases 

        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        for token in tokens: 
            if token not in operators: # If token is operand add to stack
                operand_stack.append(int(token))  # operand_stack = [-60 / 121, 17,]
                continue        
        
        # If token is operator
            else: # First calculation 
                elem2 = operand_stack.pop() # -6 / 121
                elem1 = operand_stack.pop() # 10

            if token == '+':
                operand_stack.append(elem1 + elem2)  
            elif token == '-':
                operand_stack.append(elem1 - elem2) 
            elif token == '*':
                operand_stack.append(elem1 * elem2)  
            elif token == '/':
                operand_stack.append(int(elem1 / elem2)) 
        
        return operand_stack.pop() 

