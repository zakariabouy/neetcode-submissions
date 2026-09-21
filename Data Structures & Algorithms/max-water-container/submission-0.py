class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left ,right = 0,n-1
        A=0
        while left<right:
            w=abs(left-right)
            h=min(heights[left],heights[right])
            A=max(w*h,A)
            if heights[left] >= heights[right]:
                right-=1
            else: left+=1
        print(left,right)
        return A
