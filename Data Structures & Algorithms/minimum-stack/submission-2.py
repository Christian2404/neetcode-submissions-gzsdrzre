class MinStack:
    def __init__(self):
        # Initailise stack as a list and mins as a list
        self.stack = [] # [1,2]
        self.mins = [] # [1]
        
    def push(self, val: int) -> None:
        if not self.stack: # If only value in stack 
            self.mins.append(val)

        elif val <= self.mins[-1]: # If smaller than current min append to mins
            self.mins.append(val)

        self.stack.append(val) # Add val to stack
        
    def pop(self) -> None:
        # If this value is the current min, we need to remove from the mins array as well         
        popped_item = self.stack.pop()

        if self.mins:
            if popped_item == self.mins[-1]:
                self.mins.pop()

    def top(self) -> int:
        return self.stack[-1] # Return top of stack
        
    def getMin(self) -> int:
        return self.mins[-1] # Return mins [-1]
        
