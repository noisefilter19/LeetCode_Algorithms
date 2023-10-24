class Solution {
public:
    int trap(vector<int>& height) {
        
        int n=height.size();
        vector<int> leftmax(n);
        vector<int> rightmax(n);
        leftmax[0]=height[0];
        int max=height[0];
        for(int i=1;i<n;i++){
            if(height[i]>max){
                max=height[i];
            }
            leftmax[i]=max;
        }
        
        rightmax[n-1]=height[n-1];
        max=height[n-1];
        for(int i=n-2;i>=0;i--){
            if(max<height[i]){
                max=height[i];
            }
            rightmax[i]=max;
        }
        int ans=0;
        for(int i=0;i<leftmax.size();i++){
            ans+=min(leftmax[i],rightmax[i])-height[i];
        }
        return ans;
    }
};
