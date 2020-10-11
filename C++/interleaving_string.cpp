# https://leetcode.com/problems/interleaving-string/

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
    
        int len1 = s1.size();
        int len2 = s2.size();
        if(len1+len2!=s3.size()){
            return false;
        }
        if(len1==0 and len2 == 0)
            return true;
        vector<vector<int> > v(len1+1,vector<int>(len2+1,0));
        v[0][0] = 1;
        for(int i=1;i<=len1;i++){
            if(s1[i-1]==s3[i-1])
                v[i][0]=1;
            else
                break;
        }
        for(int i=1;i<=len2;i++){
            if(s2[i-1]==s3[i-1])
                v[0][i]=1;
            else
                break;
        }
        for(int i=1;i<=len1;i++){
            for(int j=1;j<=len2;j++){
                if((v[i-1][j]==1 and s1[i-1]==s3[i+j-1]) or (v[i][j-1] and s2[j-1]==s3[i+j-1]))
                    v[i][j]=1;
            }
        }
        if(v[len1][len2]==1){
            return true;
        }else
            return false;
        
    }
};