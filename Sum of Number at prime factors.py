import math
from collections import Counter
def prime_factor(num):
    factor=[]
    while num%2==0:
        factor.append(2)
        num//=2
    for i in range(3, int(math.sqrt(num))+1,2):
        while num%i==0:
            factor.append(i)
            num//=i
    if num>2:
        factor.append(num)
    return Counter(factor)
def calculate_sum(arr, num):
    if not arr:
        return -1
    factor_count=prime_factor(num)
    total_sum=0
    n=len(arr)
    for prime, exponent in factor_count.items(): 
        if prime<n:
            total_sum+=exponent*arr[prime]
        else:
            return 0
    return total_sum
n=int(input())
arr=list(map(int,input().split()))
num=int(input())
result=calculate_sum(arr,num)
print(result)
