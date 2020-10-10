Link-https://leetcode.com/problems/employee-importance/submissions/

/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) 
    {
      int sum=0;
      Map<Integer,Employee>map=new HashMap<>();
      Queue<Employee>q=new LinkedList<>();
      for(Employee emp:employees)
      {
        map.put(emp.id,emp);
      }
      q.add(map.get(id));
      while(!q.isEmpty())
      {
        Employee curr=q.poll();
        sum+=curr.importance;
        for(int subordinate:curr.subordinates)
        {
          q.offer(map.get(subordinate));
        }
      }
      return(sum);
        
    }
}
