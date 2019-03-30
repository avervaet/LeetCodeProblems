import copy 
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_len = len(words[0])
        total_n = word_len * len(words)
        if len(s) < total_n:
            return []
        d = {}
        result = []
        for word in words:
            d[word] = d.get(word, 0) + 1
        for i in range(len(s) - total_n + 1):
            if self.checkString(s[i:i+total_n], word_len, d):
                result.append(i)
        return result
            
    def checkString(self, s, n, dico):
        d = copy.copy(dico)
        i = 0
        while i < len(s):
            current = s[i:i+n]
            if d.get(current,0):
                d[current] -= 1
            else:
                return False
            i += n
        return True
