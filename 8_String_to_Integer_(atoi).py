class Solution:
    def myAtoi(self, s: str) -> int:
        #Removing left spaces
        s = s.lstrip()
        result = ''
        s = list(s)
        sign = 1
        if s:
            if s[0] == '-':
                sign = -1
                s.pop(0)
            elif s[0] == '+':
                s.pop(0)
        else:
            return 0
        
        while s:
            if s[0].isdigit():
                result += s.pop(0)
            else:
                break
        if result:
            result = sign * int(result)
            maxN = 2**31-1
            minN = -2**31
            if result > maxN:
                result = maxN
            elif result < minN: 
                result = minN
            return result
        else:
            return 0
                