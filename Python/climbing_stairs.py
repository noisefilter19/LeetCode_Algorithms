"""
Link to Problem: https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def fibonacci(self, num):
        if num <= 1:
            return num
        return self.fibonacci(num-1) + self.fibonacci(num-2)
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fibonacci(n+1)
      
