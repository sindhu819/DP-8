'''
Leetcode- 120. Triangle - https://leetcode.com/problems/triangle/
time complexity - o(n)
space complexity - o(1)
Approach - DP - modify the original triangle top-bottom approach

'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        return min(triangle[-1])
    

# Bottom-up approach 
#time complexity - O(1)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle)-2,-1,-1):
            for j in range(0,i+1,1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
        