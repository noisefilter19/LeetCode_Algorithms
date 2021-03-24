//Problem Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

//Solution
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max= -1000000000;
        for (int i=0; i<candies.length; i++){
            if(candies[i]> max){
                max= candies[i];
            }
        }
        List<Boolean> list= new ArrayList<>();
        for (int i=0; i< candies.length; i++){
            if(candies[i]+extraCandies >= max){
                list.add(true);
            }else{
                list.add(false);
            }
        }
        return list;
    }
}