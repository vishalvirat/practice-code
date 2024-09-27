def is_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def find_smallest_prime(n):
    num=n+1 
    while not is_prime(num):
        num+=1
    return num
n=int(input()) 
result=find_smallest_prime(n)
print(result)
