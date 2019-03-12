class Solution:
    def threeSum(self, nums):
        results = []
        nums.sort();
        n = len(nums)
        for i in range(0, n - 1):  
            left = i + 1; 
            right = n - 1; 
            a = nums[i]; 
            while (left < right) : 
                b = nums[left]
                c = nums[right]
                if (a + b + c == 0):
                    results.append((a, b, c))
                    left += 1; 
                    right -= 1; 
                elif (a + b + c < 0): 
                    left += 1; 
                else: 
                    right -= 1;
        return list(set(results))