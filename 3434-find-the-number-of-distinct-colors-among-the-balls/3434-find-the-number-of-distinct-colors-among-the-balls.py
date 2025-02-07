from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        b, c, r = defaultdict(lambda : -1), defaultdict(lambda : 0), [0]
        for x, y in queries:
            cur = r[-1]
            pc = b[x]

            # If no color, set equal to y and increment c
            # If a new color, increment cur
            if pc == -1:
                b[x] = y
                c[y] += 1
            
            # If already has color, we need add these changes to c
            # Then chance in b
            else:
                c[pc] -= 1
                if not c[pc]: # If last color to exist
                    cur -= 1

                c[y] += 1
                b[x] = y
            
            if c[y] == 1: # If a new color is added
                cur += 1

            r.append(cur)
        
        return r[1:]

                
            




        