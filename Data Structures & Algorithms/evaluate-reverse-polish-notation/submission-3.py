class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n=len(tokens)
        stack=[]
        M=int(tokens[0])
        for i in range(n):
            if tokens[i]=='+':
                M=stack.pop()+stack.pop()
                stack.append(M)
            elif tokens[i]=='-':
                right=stack.pop()
                left=stack.pop()
                M=left-right
                stack.append(M)
            elif tokens[i]=='*':
                M=stack.pop()*stack.pop()
                stack.append(M)
            elif tokens[i]=='/':
                right=stack.pop()
                left=stack.pop()
                M=int(left/right)
                stack.append(M)
            else:
                stack.append(int(tokens[i]))
        return M


