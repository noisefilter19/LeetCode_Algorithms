// https://leetcode.com/problems/integer-to-roman/
class Solution {
public:
    string intToRoman(int num) {
        string num2;
        // Roman characters and their integer values
        string s[]={"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
        int n[]={1,4,5,9,10,40,50,90,100,400,500,900,1000};
        map<int,string> m;
        // Insert into a Map
        for(int i=0; i<13; i++){
            m[n[i]] = s[i];
        }
        // Reverse iteration over the map elements
        map<int, string>::iterator itr;
        for (auto itr = m.rbegin(); itr != m.rend(); itr++){
            // Loop - Nearest smallest number to num from the key in map
            while(num >= itr->first){
                num2 += itr->second;
                num = num - itr->first;
            }
        }
        return num2;
    }
};