# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    c=0
    #add code here
    freq={}
    
    for ch in str1:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
            
    for ch in str2:
        if ch not in freq:
            freq[ch]=-1
        else:
            freq[ch]-=1
            
    for v in freq.values():
        if v!=0:
            c+=abs(v)
    return c
            
    
    


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends