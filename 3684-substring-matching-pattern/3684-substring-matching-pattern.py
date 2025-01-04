class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        a, b = p.split('*')
        N, T = len(s), len(a)

        i = 0 # Only execute if a exists
        while a and i <= (N - T):

            if a == s[i:i + T]:
                s = s[i + T:]
                break
            
            # If we don't find a then 
            # regardless of b we are false
            if (i == (N - T)):
                return False

            i += 1

        if b in s: 
            return True
        return False