def min_steps_to_magic_string(s): 
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    max_freq=max(freq.values())
    min_steps=len(s)-max_freq
    return min_steps
s=input() 
result=min_steps_to_magic_string(s)
print(result)
