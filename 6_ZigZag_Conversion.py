class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [''] * numRows
        s = list(s)
        while s:
            len_s = len(s)
            for i in range(min(numRows,len_s)):
                result[i] += s.pop(0)
            len_s = len(s)
            print(result)
            for i in range(0,min(numRows-2,len_s)):
                result[numRows - i - 2] += s.pop(0)
        return ''.join(result)