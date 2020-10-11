"""
Topics: | None |
"""

SELECT name
  FROM customer
 WHERE referee_id IS NULL
    OR referee_id != 2;