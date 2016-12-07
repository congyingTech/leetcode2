'''
Created on 2016年12月7日

@author: wangcongying
'''
#-*-coding:utf-8-*-
#最长递增子序列:5, 3, 4, 8, 6, 7, 9 的最长递增子序列是3,4,6,7,9 所以得到的长度是5

def lis(nums):
    res = 1
    lenOfNums = len(nums)
    d = [0]*lenOfNums
    for i in range(lenOfNums):
        d[i] = 1
        for j in range(i):
            if nums[j]<nums[i] and d[j]+1>d[i]:
                d[i] = d[j]+1
        if d[i]>res:
            res = d[i]
    print(d)
    return res

if __name__ == "__main__":
    nums = [5, 3, 4, 8, 6, 7, 9]
    print(lis(nums))






