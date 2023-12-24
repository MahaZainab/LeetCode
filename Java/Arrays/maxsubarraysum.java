class maxsubarraysum{
    public static void calmaxsubarraysum(int numbers[]){
        int curr_sum=0;
        int max_sum=Integer.MIN_VALUE;
        
        for(int i=0; i<numbers.length; i++){
            for(int j=i; j<numbers.length; j++){
                curr_sum=0;
                for(int k=i; k<=j; k++){
                    curr_sum+=numbers[k];
                    //System.out.print( numbers[k]+ " ");
                }
                System.out.println(curr_sum);
                if(max_sum< curr_sum){
                    max_sum=curr_sum;
                }
            }

        }
        System.out.println(max_sum);
    }
    public static void main(String args[]){
        int  nums[]={2,4,6,7,20};
        calmaxsubarraysum(nums);
    }
}