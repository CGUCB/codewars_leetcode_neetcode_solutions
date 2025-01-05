class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        if len(answerKey) <= k: 
            return k

        M, N = 0, len(answerKey)
        L, R = 0, k
        T = sum([1 for i in answerKey[:k] if i == 'T'])
        F = k - T

        while R < N:

            # Adding in incremented R
            if answerKey[R] == 'T':
                T += 1
            else:
                F += 1

            # Incrementing L if invalid
            while min(T, F) > k:
                if answerKey[L] == 'T':
                    T -= 1
                else:
                    F -= 1
                L += 1
            
            M = max(M, R - L)
            R += 1
            
        return M + 1


        