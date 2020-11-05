
vector<int>v1;
class Solution {
public:
    void inside_faith(int i,int n){
        if(i>n){
            return;
        }
        v1.push_back(i);
        for(int j=0;j<=9;j++){
            int num=10*i+j;
            inside_faith(num,n);
            
        }
        
    }
    vector<int> lexicalOrder(int n) {
        v1.clear();
        if(n<=9){
            for(int k=1;k<=n;k++){
                 v1.push_back(k);
                
            }
        }
        else{
             for(int i=1;i<=9;i++){
            inside_faith(i,n);
        }
        }
        
        return v1;
       
        
    }
};
