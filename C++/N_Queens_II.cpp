class Solution {
public:
    public:
    int N;
    bool col[25];
    map < int , int > mp1;
    map < int , int > mp2;

    int dfs( int x ) {
        if( x > N )
            return 1;
        int ans = 0;
        for( int i = 1; i <= N; i ++ )
            if( ! col[i] && ! mp1[x + i] && ! mp2[x - i] ) {
                col[i] = 1;
                mp1[x + i] = 1;
                mp2[x - i] = 1;
                ans += dfs( x + 1 );
                col[i] = 0;
                mp1[x + i] = 0;
                mp2[x - i] = 0;
            }
        return ans;
    }
    
    int totalNQueens(int n) {
        N = n;
        return dfs( 1 );
    }
};
