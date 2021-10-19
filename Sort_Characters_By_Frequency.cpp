// Given a string, sort it in decreasing order based on the frequency of characters.

// Example 1:
// Input:
// "tree"

// Output:
// "eert"


class Solution {
public:
        
    string frequencySort(string s) {
      
      if(s.size() == 0)	 return "";
           unordered_map<char,int> counter;
           for(auto x : s){
               counter[x]++;                  
           } 
            sort(s.begin(),s.end(),
        	[&](char a, char b){return counter[a] > counter[b] || (counter[a] == counter[b] && a < b);}
        	);
            return s;
    }
        
     
};