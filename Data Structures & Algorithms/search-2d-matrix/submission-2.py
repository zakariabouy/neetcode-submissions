class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix) # rows
        m=len(matrix[0]) # columns
        left,right=0,n-1
        while left <= right:
            mid = (right+left)//2
            if matrix[mid][m-1] == target:
                return True
            elif matrix[mid][m-1] > target:
                right=mid-1
            else:
                left=mid+1
        row = left
        l,r=0,m-1
        if row >= n:
            return False
        while l <= r:
            mid = (r+l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l=mid+1
            else:
                r=mid-1
        return False       
        