#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        c = 0
        temp = N
        while temp>0:
            digit = temp % 10
            if digit != 0 and N % digit == 0:
                c += 1
            temp //= 10
            
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")
# } Driver Code Ends