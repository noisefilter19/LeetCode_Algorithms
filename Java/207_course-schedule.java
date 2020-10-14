// https://leetcode.com/problems/course-schedule/

import java.util.*;

class Solution {
public static boolean canFinish(int numCourses,int[][] prerequisites){
        if (prerequisites == null || prerequisites.length == 0) return true;
        
        //Will hold the graph
        HashMap<Integer,List<Integer>> adjacencyList = new HashMap<>();
        
		//pred[i] will hold the number of predecessors (prerequisites) there are for a given course
        int[] pred = new int[numCourses];
        
        //Build the graph and the predecessor counter
        for (int i = 0 ; i < prerequisites.length ; i = i + 1){
            int[] coursePair = prerequisites[i];
            
            int course = coursePair[0];
            int prereqCourse = coursePair[1];
            
            if (adjacencyList.get(course) == null) adjacencyList.put(course,new ArrayList<Integer>());
            
            adjacencyList.get(course).add(prereqCourse);
			
			//For each pair of courses you come upon [course,coursePrequisiteCourse], the number of prerequisites for the 
            pred[prereqCourse] += 1;
        }
        
        //If predecessor[i] = 0, that means that course does not have any prerequisites, add it to be processed next
        for (int i = 0 ; i < pred.length ; i++){
            
            if (pred[i] == 0){
                explore(i,adjacencyList,pred);
            }
            
        }
        
        //If there are any unexplored nodes in the graph, there is a cycle and you can't finish all courses
        for (int i = 0 ; i < pred.length ; i++){
            if (pred[i] != 0) return false;
        }
        
        return true;

    }

    //For the node that you pass in, you decrement all the predecessor counts on nodes that come after this one
    //If a given node during that has no more neighbors, you explore it
    
    //After you explore a given node, you remove it from the graph by setting its list of neighbors to null. Use this to keep track of nodes you've visited and to avoid going through old ones.
    public static void explore(int currentNode, HashMap<Integer,List<Integer>> graph, int[] predecessors){
        
        if (graph.get(currentNode) == null) return;
        
        for (Integer neighbor : graph.get(currentNode)){
            
            if (predecessors[neighbor] - 1 >= 0) predecessors[neighbor] = predecessors[neighbor] - 1;
            
            if (predecessors[neighbor] == 0) {
                explore(i,graph,predecessors);
            }
            
        }
        
        graph.put(currentNode,null);
    }

    public static void main(String args[]) {
        int numCourses =2;
        int prerequisites[][] = {{1,0},{0,1}};
        System.out.println(canFinish(numCourses, prerequisites));
    }
}