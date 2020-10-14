#https://leetcode.com/problems/queue-reconstruction-by-height/submissions/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))
        print(people)
        sorted_queue = []
        for person in people:
            sorted_queue.insert(person[1], person)
        return sorted_queue
                
        
