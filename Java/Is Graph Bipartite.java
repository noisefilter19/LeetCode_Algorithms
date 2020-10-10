Link-https://leetcode.com/problems/is-graph-bipartite/submissions/

class Solution {
    public boolean isBipartite(int[][] graph) 
    {
      int v=graph.length;
      int colour[];
      colour=new int[v];
      
      for(int i=0;i<v;i++)
      {
        if(colour[i]==1 || colour[i]==-1)
        {
          continue;
        }
        
        Queue<Integer>q=new LinkedList<>();
        q.add(i);
        colour[i]=1;
        
        while(!q.isEmpty())
        {
          int front=q.poll();
          for(int next:graph[front])
          {
            if(colour[next]==0)
            {
              colour[next]=-colour[front];
              q.add(next);
            }
            
            if(colour[next]==colour[front])
            {
              return(false);
            }
          }
        }
      }
        return(true);
    }
}
