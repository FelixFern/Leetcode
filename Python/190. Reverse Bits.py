class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        processed = "0" * (32 - len(binary)) + str(binary)
        return int(processed[::-1], 2)
