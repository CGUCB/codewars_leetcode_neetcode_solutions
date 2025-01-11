class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c, odd = Counter(s), 0
        for v in c.values():
            if v % 2:
                odd += 1
        if (odd <= k <= len(s)):
            return True
        return False