def most_freq(s):
    vowels ="aeiou"
    freq={vowel:s.lower().count(vowel) for vowel in vowels}
    max_freq=max(freq.values())
    most_freq_vowels=[vowel for vowel, frequency in freq.items() if frequency==max_freq and frequency>0]
    return most_freq_vowels[0] if most_freq_vowels else None
s=input()
print(most_freq(s))
