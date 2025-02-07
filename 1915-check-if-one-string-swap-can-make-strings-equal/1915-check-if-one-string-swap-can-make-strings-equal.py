class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = ""
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            elif not c: # First time unequal
                c = c2 + c1
            elif c == c1 + c2: # Second time and equal
                c = 'aaa'
            else: # Set c to non-matchable string because only want one swap
                return False
        return True if ((not c) or (c == 'aaa')) else False