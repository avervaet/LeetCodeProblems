import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Adding some anchor to check the exact match
        p='^' + p + '$'
        #Transforming p into regex
        p = re.compile(p)
        #Checking match and returning result
        return True if p.match(s) else False