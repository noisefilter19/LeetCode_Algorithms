class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low=0, mid=0, high=nums.size()-1;
        while(mid <= high){
            switch(nums[mid]){
                case 0:
                    swap(nums[mid++], nums[low++]);
                    break;
                case 1:
                    mid++;
                    break;
                default:
                    swap(nums[mid],nums[high--]);
                    
            }
        }
    }
};

/*
* Hint : If asked to sort array of 3 numbers(elements) only
* Variation of dutch national flag problem
*/
