# 684. Redundant Connection
# Problem link - https://leetcode.com/problems/redundant-connection/


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #init
        parent  = {}
        final = []
        
        #find function in the union find data structure
        def find(x):
            while parent[x]!=x:
                x = parent[x]
            return x
        #Union function in the union find data structure
        def union(x,y):
            root = find(x)
            parent[root] = find(y)
        
        #iterate through edges given
        for edge in edges:
            #The base case
            #If both vertices have already been seen
            #Check if they both have the same parent
            #If they do add the edge to the final list
            #if not update the graph
            if edge[0] in parent and edge[1] in parent:
                if find(edge[0]) == find(edge[1]):
                    final.append(edge)
                else:
                    union(edge[1],edge[0])
            else:
                #The rest is almost the same as the usual union find building
                #Except for some modifications done to account for some edge cases
                if edge[0] not in parent:
                    parent[edge[0]] = edge[0]
                    if edge[1] in parent:
                        union(edge[0],edge[1])
                    else:
                        parent[edge[1]] = edge[0]    
                        union(edge[1],edge[0])
                else:        
                    parent[edge[1]] = edge[0]    
                    union(edge[1],edge[0])
        return final[len(final)-1] if len(final) > 0 else []