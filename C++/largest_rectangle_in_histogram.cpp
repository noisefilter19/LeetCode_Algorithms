//https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int>s;
        int area_with_top=0;
        int area=0;
        int i=0;
        int n=heights.size();
        while(i<n){
            if(s.empty() || heights[s.top()]<=heights[i]){
                s.push(i++);
            }
            else{
                int tp=s.top();
                s.pop();
                area_with_top=heights[tp]*(s.empty()?i:i-s.top()-1);
                if(area<area_with_top)
                    area=area_with_top;
            }
        }
        while(!s.empty()){
            int tp=s.top();
            s.pop();
            area_with_top=heights[tp]*(s.empty()?i:i-s.top()-1);
            area=max(area,area_with_top);
        }
        return area;
    }
};