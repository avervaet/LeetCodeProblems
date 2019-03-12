#Definitely not my cleanest code lots of things to improve.
class Solution:
    def fourSum(self, nums, target: int):
        results = []
        nums.sort();
        n = len(nums)
        for i in range(0, n - 1):
            for j in range(i+1, n-2):
                left = i + 1; 
                right = n - 1;
                if left == j:
                    left += 1
                if right == j:
                    right -= 1
                a = nums[i]; 
                b = nums[j]
                while (left < right) : 
                    if left == j:
                        left += 1
                        continue
                    if right == j:
                        right -= 1
                        continue
                    c = nums[left]
                    d = nums[right]
                    if (a + b + c + d== target):
                        results.append(tuple(sorted((a, b, c, d))))
                        left += 1; 
                        right -= 1; 
                    elif (a + b + c + d < target): 
                        left += 1
                    else: 
                        right -= 1;


        return list(set(results))