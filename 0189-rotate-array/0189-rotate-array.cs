public class Solution {
    public void Rotate(int[] nums, int k) {
        k = k % nums.Length;

        this.RotateArr(nums, 0, nums.Length - 1);
        this.RotateArr(nums, 0, k - 1);
        this.RotateArr(nums, k, nums.Length - 1);

    }


    public void RotateArr(int[] target, int start, int end){

        while(start < end){
            int aux = target[start];
            target[start] = target[end];
            target[end] = aux;
            end-=1;
            start+=1;
        }
    }
}