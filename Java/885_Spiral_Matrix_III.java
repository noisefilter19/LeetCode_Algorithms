//Problem Link: https://leetcode.com/problems/spiral-matrix-iii/


//Solution


class Solution {
    public int[][] spiralMatrixIII(int R, int C, int r0, int c0) {
        int[][] res = new int[R*C][2];
        int i=0;
        res[i++] = new int[]{r0, c0};
        
        int len=0;
        int d=0;
        int[] directions = {0, 1, 0, -1, 0};
        
        while(i < R*C){
            if(d==0 || d==2){
                len++;
            }
            
            for(int k=0; k<len; k++){
                r0 += directions[d];
                c0 += directions[d + 1];
                if(r0<R && r0>=0 && c0<C && c0>=0){
                    res[i++] = new int[]{r0, c0};
                }
            }
            
            d = ++d % 4;
            
        }
        return res;
    }
}