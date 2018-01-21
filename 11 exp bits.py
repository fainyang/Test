
def solution( exponent):
    # write code here
    if exponent == 0:
        return 1
    if exponent == 1:
        return 11
    if exponent == -1:
        return 1/11
    
    ans = solution(exponent >> 1)
    print(exponent,ans)
    ans = ans * ans
    if exponent & 1 == 1: #奇数补充一次
        ans = ans * 11
    
    return ans

def mod(ans):
    n=len(str(ans))
    i=0
    count=0
    while (i<n):
    	mod=ans%10
    	if mod==1:
    		count+=1
    	ans=ans//10
    	i+=1
    return count

