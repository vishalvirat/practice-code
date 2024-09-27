def two_sum(nums, target):
    num_dict={}
    for i,num in enumerate (nums):
        diff=target-num
        if diff in num_dict:
            return [num_dict[diff],i]
        num_dict[num]=i
    return []
nums=list(map(int,input().split()))
target=int(input())
print(two_sum(nums,target))
