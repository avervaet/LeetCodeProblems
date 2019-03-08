class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        result = int(str(x)[::-1])
        if result >= 2147483647:
            return 0
        return sign * result
        