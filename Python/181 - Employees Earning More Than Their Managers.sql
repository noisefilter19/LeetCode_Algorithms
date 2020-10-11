"""
Topics: | None |
"""

SELECT employee.Name AS `Employee`
  FROM Employee employee
       INNER JOIN Employee manager
       ON employee.ManagerId = manager.Id
       AND employee.Salary > manager.Salary;
