class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N % 2 == 1: # Valid string can never be odd
            return False

        pre, suf = 0, 0
        for i in range(N):
            if locked[i] == '0': # Prefix
                pre += 1
            elif s[i] == ')':
                pre -= 1
            else:
                pre += 1
            
            if locked[N - i - 1] == '0': # Suffix
                suf += 1
            elif s[N - i - 1] == '(':
                suf -= 1
            else:
                suf += 1
            
            if (pre < 0) or (suf < 0): # Failure Case
                return False
        
        return True