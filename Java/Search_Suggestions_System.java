1268. Search Suggestions System

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]



class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        List<List<String>> res=new ArrayList<>();
        TreeMap<String,Integer> map=new TreeMap<>();
        Arrays.sort(products);
        List<String> plist=Arrays.asList(products);
        for(int i=0;i<products.length;i++)
            map.put(products[i],i);
        String key="";
        for(char c: searchWord.toCharArray()){
            key+=c;
            String ceiling=map.ceilingKey(key);
            String floor=map.floorKey(key+"~");
            if(ceiling==null|| floor==null)break;
            res.add(plist.subList(map.get(ceiling), Math.min(map.get(ceiling) + 3, map.get(floor) + 1)));
        }
        while (res.size() < searchWord.length()) res.add(new ArrayList<>());
        return res;
    }
}
