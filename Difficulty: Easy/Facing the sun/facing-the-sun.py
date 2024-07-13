#User function Template for python3
class Solution:
    
    def countBuildings(self,h, n):
        # code here
        cur_max=0
        count=0
        
        for num in h:
            if num>cur_max:
                count+=1
                cur_max=num
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends