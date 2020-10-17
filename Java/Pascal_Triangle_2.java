class Solution {
    public List<Integer> getRow(int n) {
    List<Integer> tri = new ArrayList<Integer>();
    int i=0;
    while(i<n+1){
         tri.add(1);
         for(int j=i-1; j>0; j--)
            tri.set(j, tri.get(j)+tri.get(j-1));    // tri[j]<- tri[j]+tri[j-1] 
         i++;
    }
    return tri;
    }
}
