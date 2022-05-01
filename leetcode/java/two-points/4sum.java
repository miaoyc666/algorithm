class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        return nnumSum(nums,4,0,target);
    }
    // n数之和直接乱杀
    // n表示求n数之和，start表示起始位置0，target目标和
    private List<List<Integer>> nnumSum(int[] nums,int n,int start,int target){
        int size = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList();
        if(size<n || n<2) return res;
        // base case 两数之和
        if(n==2){
            int left=start,right=size-1;
            while(left<right){
                // 记录指针对应的元素方便去重
                int low = nums[left],high=nums[right];
                int sum = nums[left]+nums[right];
                if(sum<target){
                    while(left<right && nums[left]==low) left++;
                }else if(sum>target){
                    while(left<right && nums[right]==high) right--;
                }else{
                    res.add(Arrays.asList(nums[left],nums[right]));
                    while(left<right && nums[left]==low) left++;
                    while(left<right && nums[right]==high) right--;
                }
            }
        }else{
            // n>2
            // for控制重复多少次
            for(int i=start;i<size;i++){
                 List<List<Integer>> sub = nnumSum(nums,n-1,i+1,target-nums[i]);
                for(List<Integer> list:sub){
                    ArrayList<Integer> tmpList = new ArrayList();
                    tmpList.add(nums[i]);
                    // 由于返回的是接口类型，这里将接口类型集合加入到arraylist
                    tmpList.addAll(list);
                    res.add(tmpList);
                }
                // 去重
                while(i<size-1 && nums[i]==nums[i+1]) i++;
            }
        }
        return res;
    }
}