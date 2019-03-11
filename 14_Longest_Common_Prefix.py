class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ''
        if strs:
            for i in range(len(strs[0])):
                current = strs[0][i]
                for e in strs:
                    if i >= len(e):
                        return result
                    if e[i] != current:
                        return result
                result += current
        return result