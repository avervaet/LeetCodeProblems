class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        maxi = 0
        result =""
        
        #Finding odd palindrome substrings
        for i,e in enumerate(s):
            j=0
            while self.isPalindrome(s[i-j:i+j+1]):
                if 2*j + 1 > maxi:
                    result = s[i-j:i+j+1]
                    maxi = 2*j + 1
                j += 1
                if i-j < 0 or i+j+1 > len(s):
                    break
                
        #Finding even palindrome substrings       
        for i in range(1,len(s)):
            j=0
            while self.isPalindrome(s[i-j-1:i+j+1]):
                if 2*j + 2 > maxi:
                    result = s[i-j-1:i+j+1]
                    maxi = 2*j + 2
                j += 1
                if i-j-1 < 0 or i+j+1 > len(s):
                    break
        return result
            
    def isPalindrome(self, s):
        return s[::-1] == s
