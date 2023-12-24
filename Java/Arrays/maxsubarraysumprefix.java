class maxsubarraysum{
    public static void calmaxsubarraysum(int numbers[]){
        int curr_sum=0;
        int max_sum=Integer.MIN_VALUE;
        int prefix[]= new int[numbers.length];
        prefix[0]=numbers[0];
        for(int i=0; i<prefix.length; i++){
            prefix[i]= prefix[i-1]+numbers[i];

        }

        for(int i=0; i<numbers.length; i++){
            for(int j=i; j<numbers.length; j++){
                curr_sum= i==0 ? prefix[j] : prefix[j]-prefix[i-1];
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