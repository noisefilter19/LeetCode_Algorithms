public class ValidTriangle611 {
    public int triangleNumber(int[] nums) {
        int numResult = 0;
        int[] triplet = new int[3];
        for (int i = 0; i < nums.length-2; i++){
            for (int j = i+1; j < nums.length-1; j++){
                for (int k = j+1; k < nums.length; k++){
                    triplet[0] = nums[i];
                    triplet[1] = nums[j];
                    triplet[2] = nums[k];
                    numResult += isTripletTriangle(triplet);
                }
            }
        }
        return numResult;
    }

    public int isTripletTriangle(int[] triplet){
        if (triplet[0] + triplet[1] <= triplet[2])
            return 0;
        else if (triplet[0] + triplet[2] <= triplet[1])
            return 0;
        else if (triplet[1] + triplet[2] <= triplet[0])
            return 0;
        else
            return 1;
    }
}
