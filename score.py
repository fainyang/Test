from datetime import datetime,timedelta
import itertools

def get_date(date):  
    date_begin=datetime.strptime(date,'%Y%m%d')
    time=str(datetime.date(date_begin))

    date1=date_begin+timedelta(days=1)
    time1=str(datetime.date(date1))

    date2=date_begin+timedelta(days=2)
    time2=str(datetime.date(date2))

    date3=date_begin+timedelta(days=2)
    time3=str(datetime.date(date3))

    date4=date_begin+timedelta(days=2)
    time4=str(datetime.date(date4))

    return time,time1,time2,time3,time4

def credit1(L): #全勤分
    credit=0
    for i in L[0]:
        if i==1:
            credit+=1
    for j in L[1]:
        if j==1:
            credit+=1
    return credit

def credit2 (L):  #一起迟到，多扣一分
    credit=0
    for i in range(5):
        if L[0][i]==1 and L[1][i]==1:
            credit+=1
    return credit

def credit3 (L): #连续迟到，罪加一等
    credit=0
    if 0 not in L[0]:
        credit+=1
    if 0 not in L[1]:
        credit+=1
    return credit

def sumcredit(L): #累加总的操行分
    c1=credit1(L)
    c2=credit2(L)
    c3=credit3(L)
    return c1+c2+c3


def todate(L,date):
    time,time1,time2,time3,time4=get_date(date)
    record=[time+'-小费',time+'-小王',time1+'-小费',time1+'-小王',time2+'-小费',\
    time2+'-小王',time3+'-小费',time3+'-小王',time4+'-小费',time4+'-小王']
    L1=L[0]+L[1]
    for i in range(len(L1)):
        if L1[i]==1:
            record[i]+='(迟到)'
        else:
            record[i]+='(正常)'
    return record

def main(start_day,faith_score):
    Calendar=[[6,6,6,6,6],[6,6,6,6,6]] #模拟日历
    L=list(itertools.product([0,1],repeat=5)) #枚举产生
    leng=len(L)
    for i in range(leng):#两次遍历
        for j in range(leng):
            Calendar[0]=L[i]
            Calendar[1]=L[j]
            if sumcredit(Calendar)==faith_score:#判断情况
                gg=todate(Calendar,start_day)
                print(gg) #输入情况

start_day='20180304'
score=1
main(start_day, score)

