class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        /*for(int i = 0; i<k; i++)
        {
            int temp = nums[n-1];
            for(int j = n-1; j>0; j--)
            {
                int temp2 = nums[j];
                nums[j] = nums[j-1];
                nums[j-1] = temp2;
            }
            nums[0] = temp;
        }  */
    int n = nums.size();
    int *a{ new int[n]{} };
    for (int i = 0; i < n; i++) {
      a[(i + k) % n] = nums[i];
    }
    for (int i = 0; i < n; i++) {
      nums[i] = a[i];
    }
    }
};