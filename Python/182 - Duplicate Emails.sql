"""
Topics: | None |
"""

SELECT Email
  FROM Person
 GROUP BY Email
HAVING COUNT(Email) > 1;
