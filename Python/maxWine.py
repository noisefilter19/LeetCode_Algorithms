
L= [2,4,6,2,5]

def max_wine(period,left,right):
	if left==right:
		return period*L[left]
	return max(period*L[left]+max_wine(period+1,left+1,right), period*L[right]+ max_wine(period+1,left,right-1))

print( max_wine(1,0,len(L)-1)) 


 
#Todo:f change it to a DP instead of recursion
