// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<string> alertNames(vector<string> &keyName, vector<string> &keyTime)
    {
        unordered_map<string, vector<int>> mp;
        vector<string> resp;
        if (keyName.empty() || keyTime.empty())
            return resp;
        for (int i = 0; i < keyName.size(); i++)
        {
            int pos = keyTime[i].find(":");
            int ah = stoi(keyTime[i].substr(0, pos));
            int bm = stoi(keyTime[i].substr(pos + 1));
            ah = ah * 60 + bm;
            mp[keyName[i]].push_back(ah);
        }
        for (auto it = mp.begin(); it != mp.end(); it++)
        {
            sort(it->second.begin(), it->second.end());
            for (int i = 1; i < it->second.size() - 1; i++)
            {
                int duration = it->second[i + 1] - it->second[i - 1];
                if (duration <= 60)
                {
                    resp.push_back(it->first);
                    break;
                }
            }
        }
        sort(resp.begin(), resp.end());
        return resp;
    }
};

int main()
{
    Solution a;
    vector<string> name = {"alice", "alice", "alice", "bob", "bob", "bob", "bob"};
    vector<string> time = {"12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"};
    vector<string> output = a.alertNames(name, time);
    // Output: ["bob"]

    cout << "[";
    for (int i = 0; i < output.size(); i++)
    {
        if (i == output.size() - 1)
            cout << output[i];
        else
            cout << output[i] << ", ";
    }
    cout << "]" << endl;
    return 0;
}