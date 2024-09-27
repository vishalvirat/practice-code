from itertools import combinations
def count_triplets_with_product(arr,m):
    count = 0
    for triplet in combinations(arr,3):
        if triplet[0]*triplet[1]*triplet[2]==m:
            count+=1
    return count
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
result=count_triplets_with_product(arr,m)
print(result)
