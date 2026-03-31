class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '*', '/']
        operand_stack = []

        for token in tokens: 
            if token not in operators: # If token is operand add to stack
                operand_stack.append(int(token))   
        
            else: # If token is operator 
                elem2 = operand_stack.pop() 
                elem1 = operand_stack.pop() 

                if token == '+':
                    operand_stack.append(elem1 + elem2)  
                elif token == '-':
                    operand_stack.append(elem1 - elem2) 
                elif token == '*':
                    operand_stack.append(elem1 * elem2)  
                elif token == '/':
                    operand_stack.append(int(elem1 / elem2)) 
        
        return operand_stack.pop() 

