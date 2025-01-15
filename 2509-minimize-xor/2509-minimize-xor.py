class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1, b2 = list(bin(num1)[2:]), list(bin(num2)[2:])
        N1, N2 = b1.count('1'), b2.count('1')
        i = -1

        while N1 > N2: # Take away from N1 until equal to N2
            if b1[i] == '1':
                N1 -= 1
                b1[i] = '0'
            i -= 1

        while N2 > N1:
            if abs(i) == len(b1): # If at end of digit, add all 1s and break
                b1 = ['1'] * (N2 - N1) + b1
                N1 = N2
                break

            c = b1[i]
            if c == '0':
                N1 += 1
                b1[i] = '1'
            i -= 1
        
        
        return int(''.join(b1), 2)