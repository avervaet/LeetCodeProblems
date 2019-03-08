import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_len = len(nums1) + len(nums2)
        if full_len == 1:
            return self.findNext(nums1, nums2)
        for i in range(int((full_len + 1)/2)):
            current = self.findNext(nums1, nums2)
        if not full_len % 2:
            nexti = self.findNext(nums1, nums2)
            return float((nexti + current)/2)
        return float(current)
        
    def findNext(self, nums1, nums2):        
        if nums1:
            f1 = nums1[0]
        else:
            f1 = math.inf
        if nums2:
            f2 = nums2[0]
        else:
            f2 = math.inf

        if f1 < f2:
            current = nums1.pop(0)
        else:
            current = nums2.pop(0)
        return current