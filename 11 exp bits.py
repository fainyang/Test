
def solution( exponent):
    # write code here
    if exponent == 0:
        return 1
    if exponent == 1:
        return 11
    if exponent == -1:
        return 1/11
    
    ans = solution(exponent >> 1)
    #print(exponent,ans)
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



def solution1(N):
    a=[1,1]
    b=[]
    #print(a)
    for j in range(N-1):
        t=0 #进位
        a.append(0)
        a.insert(0,0)#插入两个0是因为最低位肯定是1，最高位也许有进位
        b=[]
        for i in range(len(a)-1):
            b.append((a[i]+a[i+1]+t)%10)
            t=(a[i]+a[i+1]+t)//10
        a=b
        b=list(reversed(b))
    
    return(b)

i=10000
a=solution(i)
#print(a)
#b=solution1(i)
#print(b)
    