from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        pCounter=Counter(p)
        sCounter=Counter(s[0:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter :
                res.append(i-len(p)+1)
            headLetter = s[i-len(p)+1]
            sCounter[headLetter]-=1
            if sCounter[headLetter] == 0:
                del sCounter[headLetter]
        return res
            
            
        