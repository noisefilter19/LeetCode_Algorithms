class StockPrice {
    TreeMap<Integer, Integer> map1 = new TreeMap<>();
    TreeMap<Integer, Set<Integer>> map2 = new TreeMap<>();
    
    public StockPrice() {
        map1 = new TreeMap<>();
        map2 = new TreeMap<>();
    }
    
    public void update(int timestamp, int price) {
        if(map1.containsKey(timestamp)){
            
            int oldPrice = map1.get(timestamp);
            map2.get(oldPrice).remove(timestamp);
            
            
            if(map2.get(oldPrice).size()==0){
                map2.remove(oldPrice);
            }
        }
        map1.put(timestamp, price);
        map2.putIfAbsent(price, new HashSet<>());
        map2.get(price).add(timestamp);
    }
    
    public int current() {
       return map1.get(map1.lastKey());
    }
    
    public int maximum() {
       return map2.lastKey();
    }
    
    public int minimum() {
       return map2.firstKey();
    }
}
