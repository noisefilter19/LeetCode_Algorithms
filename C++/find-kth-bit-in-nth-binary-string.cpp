#include <cmath>
class Solution {
public:
    //implementation for 'not' function
    char not_im(char c) {
        return (c == '0') ? '1' : '0';
    }
    //Solution using recursion
    char findKthBit(int n, int k) {
        if (k==1) return '0';
        int len = pow(2, n) - 1;
        int half = len/2; //length until the middle '1'
        if (k < half + 1) return findKthBit(n-1, k);
        else if (k > half + 1) return not_im(findKthBit(n-1 , len - k + 1));
        return '1';        //equals half + 1
    }
};

