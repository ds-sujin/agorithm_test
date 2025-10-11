class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        i = 0
        j = 0
        while i < (len(x)//2):
            if x[i] == x[-i-1]:
                j += 0
                i += 1
            else:
                j += 1
                i += 1
        
        if j == 0 :
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
        