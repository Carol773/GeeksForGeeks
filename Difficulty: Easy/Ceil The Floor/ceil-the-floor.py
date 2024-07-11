#User function Template for python3



def getFloorAndCeil(arr, n, x):
    # code here
    min_num=-1
    max_num=-1
    min_idx=float('inf')
    max_idx=float('inf')
    
    for num in arr:
        if num<=x and (x-num)<min_idx:
            min_num=num
            min_idx=x-num
            
        if num>=x and (num-x)<max_idx:
            max_num=num
            max_idx=num-x
            
    return min_num, max_num
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends