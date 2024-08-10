#User function Template for python3

class Solution:
    def getAngle(self, H , M):
        # code here
        if H==12:
            H=0
        if M==60:
            M=0
            H+=1
            if H>12:
                H=H-12
                
        hour_angle=0.5*(H*60+M)
        min_angle=6*M
        
        angle_diff=abs(hour_angle-min_angle)
        
        angle=min(360-angle_diff,angle_diff)
        return int(angle)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        H,M=map(int,input().split())
        
        ob = Solution()
        print(ob.getAngle(H,M))
# } Driver Code Ends