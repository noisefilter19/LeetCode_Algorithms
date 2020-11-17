// https://leetcode.com/problems/course-schedule/

class Solution {
public:
    vector<int> temp;
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int inDegree[numCourses];
        for(int i=0; i<numCourses; i++)
            inDegree[i]=0;
        
        vector<int> adj_list[numCourses];

        for(int i=0; i<prerequisites.size(); i++)
            adj_list[prerequisites[i][1]].push_back(prerequisites[i][0]);

        for(int i=0; i<prerequisites.size(); i++)
            inDegree[prerequisites[i][0]]++;


        queue<int> q;
        for(int i=0; i<numCourses; i++)
            if(inDegree[i]==0)
                q.push(i);

        while(!q.empty()){
            int curr = q.front();
            temp.push_back(curr);
            q.pop();

            for (auto it = adj_list[curr].begin(); it!=adj_list[curr].end(); it++)
            {
                inDegree[*it]--;
                if(inDegree[*it]==0){
                    q.push(*it);
                }
            }
        }

        return temp.size()==numCourses;
    }
};