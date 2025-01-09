class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixSuffix(s1: str, s2: str) -> bool:
            N1, N2 = len(s1), len(s2)
            if N1 > N2:
                return False
            for i in range(N1):
                if s1[i] != s2[i]:
                    return False
                if s1[N1 - i - 1] != s2[N2 - i - 1]:
                    return False
            return True

        r = 0
        for j in range(len(words)):
            for i in range(j):
                r += isPrefixSuffix(words[i], words[j])
        return r
