#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        return sum([int(d)**3 for d in str(n)]) == n


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends