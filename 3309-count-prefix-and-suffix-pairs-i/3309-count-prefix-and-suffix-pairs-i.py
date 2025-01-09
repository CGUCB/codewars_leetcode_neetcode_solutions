class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixSuffix(s1: str, s2: str) -> bool:
            N1, N2 = len(s1), len(s2)
            if N1 > N2:
                return False
            return (s1 == s2[:N1]) and (s1 == s2[-N1:])

        r = 0
        for j in range(len(words)):
            for i in range(j):
                r += isPrefixSuffix(words[i], words[j])
        return r
