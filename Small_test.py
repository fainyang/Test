# -*- coding: utf-8 -*-
"""通过数组交换的快速排序"""
import random


def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)
        print(arr)


def partition(arr, left, right):
    """找到基准位置, 并返回"""
    pivot_index = left
    pivot = arr[left]

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    # 将基准值移动到正确的位置
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    print(pivot_index)
    return pivot_index

def rand_number(n):
    arr=[]
    for i in range(n):
         arr.append(random.randint(0, n))
    return arr

if __name__ == '__main__':
    L=rand_number(10)
    print (L)
    quicksort(L, 0, len(L)-1)
    print (L)
'''

#解决(Python)
    
    #!/usr/bin/env python
    #coding:utf-8
    
    #方法1
    
    def quickSort(arr):
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]      #将第一个值做为基准
            for i in arr:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotList.append(i)
    
            less = quickSort(less)      #得到第一轮分组之后，继续将分组进行下去。
            more = quickSort(more)
    
            return less + pivotList + more
    
    #方法2
    # 分为<, >, = 三种情况，如果分为两种情况的话函数调用次数会增加许多，以后几个好像都有相似的问题
    # 如果测试1000个100以内的整数，如果分为<, >=两种情况共调用函数1801次，分为<, >, = 三种情况，共调用函数201次
    def qsort(L):
        return (qsort([y for y in L[1:] if y <  L[0]]) + L[:1] + [y for y in L[1:] if y == L[0] + qsort([y for y in L[1:] if y > L[0]])) if len(L) > 1 else L
    
    #方法3
    #基本思想同上，只是写法上又有所变化
    
    def qsort(list):
        if not list:
            return []
        else:
            pivot = list[0]
            less = [x for x in list     if x <  pivot]
            more = [x for x in list[1:] if x >= pivot]
            return qsort(less) + [pivot] + qsort(more)
    
    #方法4
    
    from random import *
    
    def qSort(a):
        if len(a) <= 1:
            return a
        else:
            q = choice(a)       #基准的选择不同于前，是从数组中任意选择一个值做为基准
            return qSort([elem for elem in a if elem < q]) + [q] * a.count(q) + qSort([elem for elem in a if elem > q])
    
    
    #方法5
    #这个最狠了，一句话搞定快速排序，瞠目结舌吧。
    
    qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]
    
    
    if __name__=="__main__":
        a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
        print quickSort(a)
        print qSort(a)
    
        print qs(a)
'''
