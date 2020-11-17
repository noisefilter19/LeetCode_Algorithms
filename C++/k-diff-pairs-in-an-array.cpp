#include <map>
#include <set>
#include <algorithm>
class Solution
{
public:
  int findPairs(vector<int> &nums, int k)
  {
    unordered_set<int> s(nums.begin(), nums.end());
    int cnt = 0;
    if (k < 0)
      return 0;
    else if (k > 0)
    {
      for (auto i = s.begin(); i != s.end(); i++)
      {
        if (s.find((*i) + k) != s.end())
          cnt++;
      }
    }
    else
    {
      for (auto i = s.begin(); i != s.end(); i++)
      {
        cnt += count(nums.begin(), nums.end(), (*i)) > 1 ? 1 : 0;
      }
    }
    return cnt;
  }
};
