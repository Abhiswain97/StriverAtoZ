class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        count_dict = {e: 0 for e in range(1, len(arr)+1)}
        
        for e in arr:
            count_dict[e] += 1
            
        return count_dict.values()




#{ 
 # Driver Code Starts
# Main code to read input and process each test case
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().frequencyCount(arr)  # find the frequencies

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print the result
    else:
        print("[]")  # Print empty list if no valid frequencies

# } Driver Code Ends