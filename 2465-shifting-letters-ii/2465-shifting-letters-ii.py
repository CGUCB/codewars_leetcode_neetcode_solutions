class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        N = len(s)
        p = [0] * (N + 1)
        res = []

        for st, e, d in shifts:
            if d == 1:
                p[st] += 1
                p[e + 1] -= 1
            else:
                p[st] -= 1
                p[e + 1] += 1
        
        for i in range(1, N):
            p[i] += p[i - 1]
        
        for i, c in enumerate(s):
            ind = (ord(c) - 97 + p[i]) % 26
            res.append(chr(ind + 97))
        
        return ''.join(res)