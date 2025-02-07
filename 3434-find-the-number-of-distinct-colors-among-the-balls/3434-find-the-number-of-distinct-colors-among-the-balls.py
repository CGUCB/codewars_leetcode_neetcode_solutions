from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        b, c, r = defaultdict(lambda : -1), defaultdict(lambda : 0), [0] + [None] * len(queries)

        for i, (x,y) in enumerate(queries):
            cur = r[i]
            pc = b[x]
            
            # If already has color, we need add these changes to c
            # Then chance in b
            if pc != -1:
                c[pc] -= 1
                if not c[pc]: # If last color to exist
                    cur -= 1

            b[x] = y
            c[y] += 1
            if c[y] == 1: # If a new color is added
                cur += 1

            r[i + 1] = cur
        
        return r[1:]

                
            




        