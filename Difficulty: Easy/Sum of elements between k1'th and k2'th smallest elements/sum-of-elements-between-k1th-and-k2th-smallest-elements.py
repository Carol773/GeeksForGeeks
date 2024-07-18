#User function Template for python3

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        lst=sorted(A)
        sumele=0
        first=lst[K1-1]
        second=lst[K2-1]
        
        for num in A:
            if num>first and num<second:
                sumele+=num
        return sumele


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        sz = [int(x) for x in input().strip().split()]
        k1, k2 = sz[0], sz[1]
        ob=Solution()
        print( ob.sumBetweenTwoKth(a, n, k1, k2) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends