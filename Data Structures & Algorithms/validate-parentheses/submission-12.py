class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        my_stack=[]
        
        for i in range(n):
            if s[i] in ('[','(','{'):
                my_stack.append(s[i])
            else:
                if s[i] in (']',')','}') and my_stack==[]:return False
                elif s[i]==']' and my_stack[-1]=='[': my_stack.pop()
                elif s[i]==')' and my_stack[-1]=='(': my_stack.pop()
                elif s[i]=='}' and my_stack[-1]=='{': my_stack.pop()
                else: return False
        return my_stack == []