/*
LeetCode link: https://leetcode.com/problems/the-skyline-problem/
Difficulty: hard

Solution author: Gianluca Gippetto
*/
import java.util.*;


class Solution {
    static int LEFT = 0;
    static int RIGHT = 1;
    static int HEIGHT = 2;
    
    static class Corner {
        int x;
        int height;
        boolean isRightCorner;
        
        Corner(int x, int height, boolean isRightCorner) {
            this.x = x;
            this.height = height;
            this.isRightCorner = isRightCorner;
        }

        @Override
        public String toString() {
            return String.format("Corner(x: %d, height: %d, isRightCorner: %d)", x, height, isRightCorner);
        }
    }
    
    static <T> T last(List<T> list) {
        return list.get(list.size() - 1);
    }
    
    static void heapPop(PriorityQueue<Corner> heap, Map<Integer, LinkedList<Corner>> heightToItems) {
        Corner removed = heap.poll();
        heightToItems.get(removed.height).remove(removed);
    }
    
    static void heapPush(PriorityQueue<Corner> heap, Map<Integer, LinkedList<Corner>> heightToItems, Corner corner) {
        heap.add(corner);
        if (!heightToItems.containsKey(corner.height)) 
            heightToItems.put(corner.height, new LinkedList<Corner>());
        heightToItems.get(corner.height).push(corner);
    }
        
    public List<List<Integer>> getSkyline(int[][] buildings) {
        if (buildings.length == 0)
            return  new ArrayList<>(1);

        List<Corner> corners = new ArrayList<>(buildings.length * 2);
        int lastHeight = -1;
        for (int[] b : buildings) {
            if (b[HEIGHT] == lastHeight) {
                last(corners).x = b[RIGHT];
            } else {
                corners.add(new Corner(b[LEFT], b[HEIGHT], false));
                corners.add(new Corner(b[RIGHT], b[HEIGHT], true));
                lastHeight = b[HEIGHT];
            }
        }
        corners.sort((a, b) -> a.x - b.x);
        
        List<List<Integer>> skyline = new ArrayList<>();
        Corner firstCorner = corners.get(0);
        skyline.add(Arrays.asList(firstCorner.x, firstCorner.height));
        
        // heap.poll() returns the Corner with maximum height
        PriorityQueue<Corner> heap = 
            new PriorityQueue<>(64, (a, b) -> b.height - a.height);
			
        // Useful to remove items from the priority queue:
        Map<Integer, LinkedList<Corner>> heightToItems = new HashMap<>(); 
        
        for (Corner corner : corners) {
            int currentHeight = (!heap.isEmpty()) ? heap.peek().height : 0;
            
            if (corner.isRightCorner) {
                assert (corner.height <= currentHeight);
                if (corner.height == currentHeight) {
                    heapPop(heap, heightToItems);
                    int newHeight = (!heap.isEmpty()) ? heap.peek().height : 0;
                    List<Integer> lastKeyPoint = last(skyline);
                    if (corner.x == lastKeyPoint.get(0))
                        lastKeyPoint.set(1, newHeight);
                    else
                        skyline.add(Arrays.asList(corner.x, newHeight));
                }
                else {
                    Corner item = heightToItems.get(corner.height).pop();
                    heap.remove(item);
                }
            }
            else { // left corner of a building
                if (corner.height > currentHeight) {
                    List<Integer> lastKeyPoint = last(skyline);
                    if (corner.x == lastKeyPoint.get(0))
                        lastKeyPoint.set(1, corner.height);
                    else
                        skyline.add(Arrays.asList(corner.x, corner.height));
                }
                heapPush(heap, heightToItems, corner);
            }
        }
        return skyline;
    }
}