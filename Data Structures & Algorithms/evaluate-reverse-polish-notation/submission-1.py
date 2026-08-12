class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n=len(tokens)
        stack=[]
        M=int(tokens[0])
        for i in range(n):
            if tokens[i]=='+':
                M=stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(M)
            elif tokens[i]=='-':
                M=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(M)
            elif tokens[i]=='*':
                M=stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(M)
            elif tokens[i]=='/':
                M=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(M)
            elif tokens not in ("+", "-", "*","/") :
                stack.append(int(tokens[i]))
        return M


