n=int(input())
a=list(map(int, input().strip().split()))[:n] 
freq=dict()
for party in a:
    if party in freq.keys(): 
        freq[party]+=1

    else:
        freq[party]=1
maximum=0
answer=0
count=0
for key, value in freq.items():
    if maximum<value: 
        maximum=value 
        answer=key
for value in freq.values():
    if maximum==value:
        count+=1
if count>1:
    print(-1)
else:
    print(answer)
