class Solution:
    def isValid(self, s: str) -> bool:
        d={'(': ')', '{':'}', '[':']'}
        queu = []
        for e in s:
            if d.get(e,0):
                queu.insert(0,d[e])
            else:
                if not queu or not e == queu.pop(0):
                    return False
        if queu:
            return False
        return True