// https://leetcode.com/problems/string-to-integer-atoi/
class Solution {
   public:
    int myAtoi(string str) {
        int sign = 1, i = 0;
        while (str[i] == ' ') i++;
        if (str[i] == '-' || str[i] == '+') sign = 1 - 2 * (str[i] == '-'), i++;
        long long int base = 0;
        while (str[i] >= '0' && str[i] <= '9') {
            base = 10 * base + (str[i++] - '0');
            if (base > INT_MAX) {
                if (sign == -1) return INT_MIN;
                return INT_MAX;
            }
        }
        if (base > INT_MAX) {
            if (sign == -1)
                return INT_MIN;
            else
                return INT_MAX;
        }
        return (int)base * sign;
    }
};