public class maxarray {
    public static void calmaxarray(int numbers[]){
        int currsum=0;
        int maxsum=Integer.MIN_VALUE;
        for(int i =0; i<numbers.length;i++){
            for(int j=i; j< numbers.length; j++ ){
                currsum=0;
                for(int k=i; k<= j; k++){
                    currsum+=numbers[k];
                    
                    //System.out.print(numbers[k]+ " ");
                }
                if(maxsum<currsum){
                    maxsum=currsum;
                }
                //System.out.println();

            }
        }
        System.out.println(" The maximum sum of subarrays is: " + maxsum);
    }

    public static void main(String args[]){
        int nums[]={-1,1,6,-3,-4};
        calmaxarray(nums);

    }
    
}
