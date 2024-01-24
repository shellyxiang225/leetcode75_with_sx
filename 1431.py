class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        self = []
        max_candies = max(candies)
        for i in candies:
            if i + extraCandies >= max_candies:
                self.append(True)
            else:
                self.append(False)
        return self