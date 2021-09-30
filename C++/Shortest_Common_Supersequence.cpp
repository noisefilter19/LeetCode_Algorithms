//Problem Link
// https://leetcode.com/problems/shortest-common-supersequence/

class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        string s=find_SCS(str1,str2);
        reverse(s.begin(),s.end());
        return s;
    }
    
    string find_SCS(string str1,string str2){
        vector<vector<int>> lcs(str1.size()+1,vector<int>(str2.size()+1,0));
        for(int i=1;i<=str1.size();i++){
            for(int j=1;j<=str2.size();j++){
                if(str1[i-1]==str2[j-1])
                    lcs[i][j]=lcs[i-1][j-1]+1;
                else
                    lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1]);
            }
        }
        
        int i=str1.size();
        int j=str2.size();
        string s;
        
        while(i>0 && j>0){
            if(str1[i-1]==str2[j-1]){
                s.push_back(str1[i-1]);
                i--;j--;
            }
            else{
                if(lcs[i-1][j]>lcs[i][j-1]){
                    s.push_back(str1[i-1]);
                    i--;
                }
                else{
                    s.push_back(str2[j-1]);
                    j--;
                }
            }
        }
        
        while(i>0){
            s.push_back(str1[i-1]);
            i--;
        }
        while(j>0){
            s.push_back(str2[j-1]);
            j--;
        }
        return s;
    }
};
