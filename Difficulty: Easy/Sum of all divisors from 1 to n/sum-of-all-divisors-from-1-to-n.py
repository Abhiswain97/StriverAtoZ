#User function Template for python3

import math

class Solution:
    def sumOfDivisors(self, n):
        total_sum = 0
    	for i in range(1,N+1):
    	    total_sum += i*(N//i)
    	return total_sum
        # def F(i):
        #     divs = []
        #     for j in range(1, int(math.sqrt(i+1))):
        #         if i%j == 0: 
        #             divs.append(i)
        #             if j != i//j:
        #                 divs.append(i//j)
            
        #     return sum(divs)
        
        # s = 0
        # for i in range(1, n+1):
        #     s += F(i) 
            
        # return s
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends