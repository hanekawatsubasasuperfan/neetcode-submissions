class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1

        prev = [1,1]

        def fib(n, prev):
            if n < len(prev):
                return prev[n]
            else:
                res = fib(n-1,prev) + fib(n-2,prev)
            prev.append(res)
            return res
        
        fib(n,prev)
        return prev[n]
            