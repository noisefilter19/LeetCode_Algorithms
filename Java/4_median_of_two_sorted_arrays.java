/**
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
 * The overall run time complexity should be O(log (m+n)).
 */

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) 
    {
        // according to given constraints all numbers are in this range
        int low = (int)-1e6, high = (int)1e6 ;
        
        int n = nums1.length, m = nums2.length ;
        
        int totalLen = n + m ;
        
        int pos = totalLen/2 ;
        
        // binary search to find the element which will be present at pos = totalLen/2 
        // after merging two arrays in sorted order
        while (low <= high)
        {
            int mid = low + ((high-low)>>1) ;   
            
            // total number of elements in arrays which are less than mid
            int ub = upperBound(nums1, mid) + upperBound(nums2, mid) ;
             
            if (ub <= pos) low = mid + 1 ;
            else high = mid - 1 ;
        }
        
  
        double ans = low ;
        
        // if there are even number of elements, we will also have to 
        // find element at pos = totalLen/2 - 1
        if ((totalLen)%2 == 0)
        {
            pos-- ;
            low = (int)-1e6; high = (int)1e6 ;
            while (low <= high)
            {
               int mid = low + ((high-low)>>1) ;   
               int ub = upperBound(nums1, mid) + upperBound(nums2, mid) ;
               
               if (ub <= pos) low = mid + 1 ;
               else high = mid - 1 ;
            }
            
            // average of two elements in case of even number of elements
            ans = (ans + low*1.0)/2 ;
        }
        
        return ans ;
    }
    
    // a function which returns the index of smallest element which is strictly greater than
    // key (i.e. it returns number of elements which are less than or equal to key)
    public int upperBound(int[] arr, int key)
    {
        int low = 0, high = arr.length ;
        
        while (low < high)
        {
            int mid = low + ((high-low)>>1) ;
            
            if (arr[mid] <= key)
                low = mid + 1 ;
            else high = mid ;
        }
        
        return low ;
    }
    
}
