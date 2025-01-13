from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        r, c = 0, Counter(s)
        for _, v in c.items():
            if v % 2: # Odd num chars
                r += 1
            else: # Even num chars
                r += 2
        return r
        