'''
Leetcode- 413. Arithmetic Slices - https://leetcode.com/problems/arithmetic-slices/
time complexity - O(N)
space complexity - O(1)
Approach - recursive solution

'''

#recursive 
class Solution:
    slice=0
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        self.helper(A,0)
        return self.slice
        
        
    def helper(self, A,i):
        if i>=len(A)-2:
                return 0
        temp=0
        if A[i+1]-A[i]==A[i+2]-A[i+1]:
            temp=1+self.helper(A,i+1)
            self.slice+=temp
        else:
            self.helper(A,i+1)
        return temp
    
#dp approach 
# space - O(N)

class Solution:
    slice=0
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp=[0 for _ in range(len(A))]
        for i in range(len(A)-3,-1,-1):
            if A[i+1]-A[i]==A[i+2]-A[i+1]:
                dp[i]=1+dp[i+1]
                self.slice+=dp[i]
            
        return self.slice
    
# space = O(1)
class Solution:
    slice=0
    
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp=0
        for i in range(len(A)-3,-1,-1):
            if A[i+1]-A[i]==A[i+2]-A[i+1]:
                dp=1+dp
                self.slice+=dp
            else:
                dp=0
            
        return self.slice
        
        
        
        