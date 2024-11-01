public class Solution {

    public bool ContainsDuplicate(int[] nums) {
        
        Dictionary<int, int> hashMap = new Dictionary<int, int>();
        foreach (var number in nums)
        {
            if(!hashMap.ContainsKey(number)){
                hashMap.Add(number, 1);
            }else{
                return true;
            }
        }
        return false ;
    }

    public bool ContainsDuplicateSort(int[] nums) {
        
        //here you can implements your sort algorithm
        Array.Sort(nums);
        for(int j = 1; j < nums.Length; j++){
            if(nums[j-1] == nums[j]) return true;
        }
        return false;
    }

    public bool ContainsDuplicateWithDict(int[] nums) {
        
        Dictionary<int, int> hashMap = new Dictionary<int, int>();
        foreach (var number in nums)
        {
            if(!hashMap.ContainsKey(number)){
                hashMap.Add(number, 1);
            }else{
                return true;
            }
        }
        return false ;
    }

    public bool ContainsDuplicateQuadratic(int[] nums){
        int size = nums.Length; 
        for(int i = 0; i< size; i++){
            for(int j = i+1; j < size; j++){
                if(nums[i] == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}