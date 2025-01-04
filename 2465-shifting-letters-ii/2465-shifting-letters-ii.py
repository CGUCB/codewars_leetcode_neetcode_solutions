class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        ps = [0 for _ in range(len(s))]
        sn = [ord(c) - 97 for c in s]
        res = []

        # Put start and end of shifts in ps
        for r in shifts:
            d = r[2] if r[2] == 1 else -1    
            ps[r[0]] += d
            if (r[1] + 1) < len(ps):
                ps[r[1] + 1] -= d
        
        # Prefix sum through all shifts
        for i in range(1, len(ps)):
            ps[i] += ps[i - 1]

        # Apply to ordinal versions and 
        # convert back to strings
        for x, y in zip(sn, ps):
            c = x + y
            while c < 0:
                c += 26
            res.append(chr(97 + c % 26))
        
        return ''.join(res)