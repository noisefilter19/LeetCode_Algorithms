class Solution {
public:
    string extractWord(int &i, string A){
        string ans = "";
        while(A[i] == ' ' && i < A.size()){
            i++;
        }
        while(A[i] != ' ' && i < A.size()){
            ans = ans + A[i];
            i++;
        }
        return ans;
    }
    bool wordPattern(string pattern, string str) {
        int i = 0, j = 0;
        map<string, char> myMap;
        map<char, string> myMap1;
        
        while(i < str.size() && j < pattern.size()){
            string temp = extractWord(i, str);
            char t = pattern[j];
            if(myMap.find(temp) != myMap.end()){
                if(myMap[temp] != t){
                    return false;
                }
            }
            else{
                myMap[temp] = t;
            }
            if(myMap1.find(t) != myMap1.end()){
                if(myMap1[t] != temp){
                    return false;
                }
            }
            else{
                myMap1[t] = temp;
            }
            j++;
        }
        
        if(i < str.size() || j < pattern.size()){
            return false;
        }
        
        return true;
    }
};ś