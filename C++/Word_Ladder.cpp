class Solution {
public:

    using ll = long long;
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<pair<string, ll>> q;
        q.push({beginWord, 0});
        unordered_set<string> s;
        unordered_map<string, bool> visited;
        
        for(auto w : wordList) s.insert(w);
        
        while(!q.empty()){
            auto from = q.front();q.pop();
            if(from.first == endWord) return from.second+1;
            
            if(visited[from.first]) continue; 
            visited[from.first] = true;
            for(int i = 0; i< 26; ++i){
                char ch = 'a'+ i;
                for(int j = 0; j < from.first.size(); ++j){
                    string t = from.first;
                    char original = t[j];
                    t[j]=ch;
                    //insert new node, if not visited.
                    if(s.find(t) != s.end() && !visited[t]) q.push({t, from.second+1});
                    t[j]=original;
                }
            }
        }
        return 0;
    }
};
