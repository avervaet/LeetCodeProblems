class Solution:
    def maxArea(self, height) -> int:
        maxi = 0
        first = 0
        last = len(height) - 1
        while first < last:
            maxi = max(maxi, min(height[first], height[last]) * (last-first))
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return maxi