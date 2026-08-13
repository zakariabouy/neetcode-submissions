class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [] 
        res = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                past_day_index = stack.pop()
                res[past_day_index] = i - past_day_index
            stack.append(i)
        return res