import math
class Solution:
    def threeSumClosest(self, nums, target: int):
        closest = math.inf
        result = math.inf
        nums.sort();
        n = len(nums)
        for i in range(0, n - 1):  
            left = i + 1; 
            right = n - 1; 
            a = nums[i]; 
            while (left < right) : 
                b = nums[left]
                c = nums[right]
                local_sum = a + b + c
                if local_sum == target:
                    return target
                elif local_sum < target: 
                    left += 1; 
                else: 
                    right -= 1;  
                distance = abs(local_sum - target)
                if distance < closest:
                    result = local_sum
                    closest = distance
        return result