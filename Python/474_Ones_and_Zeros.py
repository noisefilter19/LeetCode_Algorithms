# Problem link: https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[0 for i in range(n+1)] for i in range(m+1)]	# arr[i][j] will contain the max number of strings we could include if we had i 0s allowed and j 1s allowed
        
        for s in strs:
			# After each iteration, we'll get the max number of strings we could include till that iteration
            oc = s.count('1')	# counting the number of 1s in the current string
            zc = (len(s))-oc	# counting the number of 0s in the current string
            
            for i in range(m, zc-1, -1):	# No need to go below zc or oc
                for j in range(n, oc-1, -1):
					# Either do not include the current string, in which case arr[i][j] would remain the same
					# or include the current string and arr[i][j] would become arr[i-zc][j-oc]+1
					# We'll take the max of both
                    arr[i][j] = max(arr[i][j], arr[i-zc][j-oc]+1)
        
        # for row in arr:
        #     print(row)
        
        return arr[-1][-1]
        