class Solution:
    def letterCombinations(self, digits: str):    
        results = []
        d = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'],
            '9':['w','x','y','z']}
        for digit in digits:
            print(digit)
            new_results = []

            for result in results:
                for l in d[digit]:
                    new_results.append(result + l)
            if not results:
                for l in d[digit]:
                    new_results.append(l)
            results = new_results
        return results