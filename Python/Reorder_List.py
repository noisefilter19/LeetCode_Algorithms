#143 | Reorder List | Python

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
		
		# ----------------------------------------------
		# Save linked list in array
		
        arr = []
        
        cur, length = head, 0
		
        while cur:
            arr.append( cur )
            cur, length = cur.next, length + 1
        
		# ----------------------------------------------
        # Reorder with two-pointers
		
        left, right = 0, length-1
        last = head
        
        while left < right:
            arr[left].next = arr[right]
            left += 1
            
            if left == right: 
                last = arr[right]
                break
                
            arr[right].next = arr[left]
            right -= 1
            
            last = arr[left]
        
        if last:
            last.next= None