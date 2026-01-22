from collections import Counter

class Solution:
    def maxFreqSum(self, s):
        vowels = set('aeiou')
        freq = Counter(s)
        
        # Max frequency among vowels
        vowel_freqs = [freq[c] for c in freq if c in vowels]
        max_vowel = max(vowel_freqs) if vowel_freqs else 0
        
        # Max frequency among consonants
        consonant_freqs = [freq[c] for c in freq if c not in vowels]
        max_consonant = max(consonant_freqs) if consonant_freqs else 0
        
        return max_vowel + max_consonant
