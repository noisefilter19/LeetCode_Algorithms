// 1557. Minimum Number of Vertices to Reach All Nodes


// Problem link - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/


class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {

        List<List<Integer>>  graph = new ArrayList<>();
        
        //Init adjacency list
        for(int i =0;i<n;i++)
            graph.add(new ArrayList<>());

        //Create adjacency list
         for(List<Integer> edge : edges)
        {
            graph.get(edge.get(0)).add(edge.get(1));
        }

        //Array to keep track of nodes that we have already come accross
        boolean[] visited = new boolean[n];
        
        //List to hold final answer
        List<Integer> nodes = new ArrayList<>();
        
        //Iterate through all nodes as there maybe some nodes without any edges coming into it i.e indegree = 0
        
        for (int i =0;i<graph.size();i++)
        {
            if (!visited[i])
            {
                dfs(graph,i,visited);
            }
        }
        
        for(int i =0;i<n;i++)
        {
            if (!visited[i])
                nodes.add(i);
        }
        
        return nodes;
    }
    
    
    //Main driver code
    //A point to note here is that when we do dfs on a node we are not necessarily marking that node as visited as there maybe a node in the upcoming iterations that also visits this node
    // That way we do not have to include redundant nodes and this way we obtain the minimum number of nodes 
    
    public static void dfs(List<List<Integer>>graph,int index,boolean[] visited)
    {   
        for(int nei : graph.get(index))
        {
            //Visit the neighbours of the node
            //Also visit all the neighbours of the neighbour and so on and so forth untill none remain
            if (!visited[nei])
            {
            visited[nei] = true;
            dfs(graph,nei,visited);
            }
        }
            
    }
}