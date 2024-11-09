#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here
    	res = []
    	for i in range(1, n+1):
    	    f = self.fact(i)
    	    if f > n:
    	        break
    	    res.append(f)
    	    
    	return res 
            
    def fact(self, k):
        if k <= 1:
            return 1
        else:
            return k * self.fact(k-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends