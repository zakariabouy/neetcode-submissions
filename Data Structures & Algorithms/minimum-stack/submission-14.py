class MinStack:

    def __init__(self):
        self.stack=[]
        self.stackMIN=[float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.stackMIN[-1]: self.stackMIN.append(val)

    def pop(self) -> None:
        if self.stackMIN[-1]==self.stack[-1]:self.stackMIN.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMIN[-1]
