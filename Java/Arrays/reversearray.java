public class reversearray {
    public static void reverse(int numbers[], int Marks){
        Marks+=45;
        int left=0, right=numbers.length-1;
        while(left<right){
            int swap=numbers[left];
            numbers[left]=numbers[right];
            numbers[right]=swap;
            left++;
            right--;
        }
    }
    public static void main(String args[]){
        System.out.println("This is a program to reverse the array");
        int nums[]={2,4,6,8,10};
        int Marks=30;
        reverse(nums, Marks);
        System.out.println(Marks);
        for(int i=0; i<nums.length;i++){
            System.out.print(nums[i]+" ");
        }

    }
}
