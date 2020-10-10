# https://leetcode.com/problems/number-of-islands/

# class Graph defined here which contains node_count and adjacency_matrix
class Graph:
   def  __init__(self):
        self.node_count=0
        self.adjacency_list=[]

# exploring every unexplored node of the graph recursively in a depth first way
def explore(graph,node,explored):
        if explored[node] ==False :
            explored[node]=True
            for adjacent_node in graph.adjacency_list[node]:
                explore(graph,adjacent_node,explored)
        
# checking for total no of connected components in the graph (water is exluded )
def dfs(graph,explored):
    connnected_components=0
    for i in range(0,graph.node_count):
        if explored[i] ==False :
            explore(graph,i,explored)
            connnected_components+=1 
    return connnected_components

#returns the list of nodes that are connected to nodes(i,j) 
def adjacent_elements(grid,i,j):
        al=[]
        rows=len(grid)
        cols=len(grid[0])
        
         #checks if grid[i][j] is water or not, if it is water than a vacant list is returned else valid connected nodes are appended to the list and returned
        if grid[i][j] == '1' :
            if i-1>=0 :
                if grid[i-1][j] != '0':
                    al.append((i-1)*cols+j)
            if i+1<rows:
                if grid[i+1][j] != '0':
                    al.append((i+1)*cols+j)
            if j-1>=0:
                if grid[i][j-1] != '0':
                    al.append(i*cols+j-1)
            if j+1<cols:
                if grid[i][j+1] != '0':
                    al.append(i*cols+j+1)
        return al
        
#Covnverts the grid into a graph format so that Depth First Search could be implemented easily
def grid_to_graph_converter(grid):
        graph=Graph()
        rows=len(grid)
        cols=len(grid[0])
        explored=[False for i in range(rows*cols)] # list of all the nodes that are already explored in DFS is initialised to all False
        for i in range(0,rows):
            for j in range(0,cols):
                
                if grid[i][j]=='0':
                    # Marking all the water present as already explored so that they are not explored in the Depth First Search
                    explored[i*cols+j]=True        

                graph.node_count+=1 
                graph.adjacency_list.append(adjacent_elements(grid,i,j))
        return graph,explored


class Solution:
    # Required numIslands(self,grid:list[list[str]) function is defined below
    def numIslands(self,grid):
        if len(grid) == 0:
            return 0
        graph,explored=grid_to_graph_converter(grid)
        return dfs(graph,explored)
        
        
# Driver code
# grid = [
# ["1","1","1","1","0"],
# ["1","1","0","1","0"],
# ["1","1","0","0","0"],
# ["0","0","0","0","0"]
# ]
# print(Solution().numIslands(grid))

        