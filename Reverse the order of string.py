def reverse_world(s):
    words=s.split()
    reversed_words=words[::-1]
    reversed_s=' '.join(reversed_words)
    return reversed_s
s=input()
print(reverse_world(s))
