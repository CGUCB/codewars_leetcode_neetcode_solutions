from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        b = defaultdict(lambda : -1)
        c = defaultdict(lambda : 0)
        r = [None] * len(queries)

        for i, (x,y) in enumerate(queries):

            pc = b[x]

            if pc != -1:
                c[pc] -= 1
                if not c[pc]:
                    c.pop(pc)

            b[x] = y
            c[y] += 1
            r[i] = len(c)
        
        return r 