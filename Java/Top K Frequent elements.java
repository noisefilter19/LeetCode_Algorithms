Link-https://leetcode.com/problems/top-k-frequent-elements/

class Solution {
    public int[] topKFrequent(int[] nums, int k) 
    {
      int i=0,j=0,no=0;
      Arrays.sort(nums);
      PriorityQueue<int[]>pq=new PriorityQueue<>((a,b)->(b[0]-a[0]));
      Map<Integer,Integer>map=new HashMap<>();
      int ret[];
      ret=new int[k];
      if(nums==null || nums.length==0 || k==0)
      {
        return(new int[]{});
      }
      for(i=0;i<nums.length;i++)
      {
        if(!map.containsKey(nums[i]))
        {
          map.put(nums[i],0);
        }
        map.put(nums[i],map.get(nums[i])+1);
      }
      
      for(Map.Entry<Integer,Integer>e:map.entrySet())
      {
        pq.add(new int[]{e.getValue(),e.getKey()});
      }
      j=0;
      while(!pq.isEmpty() &&  k!=0)
      {
        int []arr=pq.poll();
        ret[j++]=arr[1];
        k--;
      }
      return(ret);    
    }
}
