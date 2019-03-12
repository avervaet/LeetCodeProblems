class Solution:
    def threeSum(self, nums):
        results = []
        nums.sort();
        n = len(nums)
        for i in range(0, n - 1):  
            left = i + 1; 
            right = n - 1; 
            x = nums[i]; 
            while (left < right) : 
                if (x + nums[left] + nums[right] == 0) : 

                    results.append((x, nums[left], nums[right]))
                    left += 1; 
                    right -= 1; 
                elif (x + nums[left] + nums[right] < 0): 
                    left += 1; 
                else: 
                    right -= 1;
        return list(set(results))