class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.fib(n, memo)

    def fib(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if (n not in memo):
            memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)

        return memo[n]
