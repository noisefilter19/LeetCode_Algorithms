class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        int low = matrix[0][0], high = matrix[m-1][n-1];
        while(low < high){
            int mid = (high - low)/2 + low;
            int count = 0;
            int j = n - 1;
            for(int i = 0; i < m; i++){
                while(j >= 0 && matrix[i][j] > mid)
                    j--;
                count += j + 1;
            }
            if(count < k)
                low = mid + 1;
            else
                high = mid;
        }
        return low;
    }
}
