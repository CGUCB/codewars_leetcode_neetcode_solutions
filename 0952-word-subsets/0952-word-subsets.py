from collections import defaultdict
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d, r = defaultdict(lambda : 0), []
        for w2 in words2:
            c = Counter(w2)
            for k, v in c.items():
                d[k] = max(d[k], v)
        for w1 in words1:
            a, c = 1, Counter(w1)
            for k, v in d.items():
                if (k not in c) or c[k] < v:
                    a = 0
            if a:
                r.append(w1)
        return r