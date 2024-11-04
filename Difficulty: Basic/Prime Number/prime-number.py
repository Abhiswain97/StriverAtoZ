#User function Template for python3

import math

class Solution:
    def isPrime (self, N):
        # code here
        cnt = 0
        for i in range(1, int(math.sqrt(N)) + 1):
            if N % i == 0:
                cnt += 1
                if N//i != i:
                    cnt += 1
                    
        return 1 if cnt == 2 else 0 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
        print("~")
# } Driver Code Ends