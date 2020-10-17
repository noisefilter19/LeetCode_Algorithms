/*
Problem Link: https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

*/

class Solution {
public:
    
    void addEdge(vector<int> adj[], int u, int v){
        
        adj[u].push_back(v);
    }
    
    bool tropoSort(vector<int> adj[],int n){
        
        queue<int> q;
        vector<int> inDeg(n,0);
        for(int i=0;i<n;i++){
            for(auto x: adj[i])
                inDeg[x]++;
        }
        
        for(int i=0;i<n;i++){
            if(inDeg[i]==0)
                q.push(i);
        }
        
        int count =0;
        while(!q.empty()){
            int curr= q.front();
            q.pop();
            count++;
            
            for(auto x: adj[curr]){
                 if(--inDeg[x]==0)
                     q.push(x);
            }
        }
        if(count==n)
            return true;
        return false;
        
    }
    
    bool canFinish(int n, vector<vector<int>>& A) {
        
        if(n==1)
            return true;
         int m = A.size();
        if(m==0)
            return true;
        
        vector<int> adj[n];
       
        for(int i=0;i<m;i++){
            
            addEdge(adj,A[i][0], A[i][1]);
        }
        
        return tropoSort(adj,n);
        
    }
};
