def find_equi(a):
    n=len(a)
    total_sum=sum(a)
    left_sum=0
    for i in range(n):
        right_sum=total_sum-left_sum-a[i] 
        if left_sum==right_sum:
            return i+1
        left_sum+=a[i]
    return "NOT FOUND"
n=int(input())
a=list(map(int,input().split()))
result=find_equi(a)
print(result)
