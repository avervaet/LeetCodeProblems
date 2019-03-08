class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        d = {}
        for i,e in enumerate(s):
            if e in d.keys():
                return max(self.lengthOfLongestSubstring(s[d[e]+1:]), count)
            d[e] = i
            count += 1
        return count
