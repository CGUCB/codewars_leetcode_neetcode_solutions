class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        r = 0
        for d in derived:
            r ^= d
        return not r