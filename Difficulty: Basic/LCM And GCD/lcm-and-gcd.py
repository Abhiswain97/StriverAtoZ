#User function Template for python3

class Solution:
    def lcmAndGcd(self, a , b):
        # code here 
        
        temp_a = a
        temp_b = b
        
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
               
        gcd = a if a > 0 else b       
        lcm = (temp_a*temp_b)//gcd
        
        return lcm, gcd
        
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        ob = Solution()
        ptr = ob.lcmAndGcd(A, B)

        print(ptr[0], ptr[1])
        print("~")

# } Driver Code Ends