// https://leetcode.com/problems/course-schedule/

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        /*
    To complete a course if you find  the same course again to complete then you are stuck inside a cycle.
    
    Cycle detection algorithm for Graph using DFS (Graph coloring algorithm)
    Each node has 3 states, 0 = not processed, 1 = processed, 2 = processing
    Getting a processing node while processing any other node is a cycle is the main logic here.
    */
        vector<int> visited(numCourses, 0);
        vector<vector<int>> adj(numCourses);
        for (auto course : prerequisites)
            adj[course[0]].push_back(course[1]); // this is adjacency matrix

        for (int i = 0; i < numCourses; i++)
        {
            if (visited[i] == 1)
                continue; // already processed

            if (isCycle(i, adj, visited))
                return false; // if cycle found then just return false
        }
        return true;
    }
    bool isCycle(int course, vector<vector<int>> &adj, vector<int> &visited)
    {
        if (visited[course] == 2)
            return true; // is processing but encountered so a cycle found

        visited[course] = 2; // mark it as processing
        for (auto couse_to_take : adj[course])
        {
            if (isCycle(couse_to_take, adj, visited))
                return true;
        }
        visited[course] = 1; // mark it as processed
        return false;
    }
};

int main()
{
    Solution a;
    int numCourses = 2;
    vector<vector<int>> prerequisites = {{1, 0}, {0, 1}};
    cout << a.canFinish(numCourses, prerequisites); //Output: false
    /*
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0,
                 and to take course 0 you should also have finished course 1. So it is impossible.
    */
    return 0;
}