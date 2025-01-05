import math
class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        N = len(grades)
        return int((-1 + math.sqrt(1 + 8 * N)) / 2)

        