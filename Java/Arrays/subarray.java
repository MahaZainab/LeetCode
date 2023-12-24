public class subarray {

    public static void calsubarray1(int numbers[]){
        for(int i=0; i< numbers.length; i++){
            int start= i;
            for(int j=i; j<numbers.length; j++){
                int end=j;
                for( int k = start; k <= end; k++){
                    System.out.print(numbers[k]+ " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
    public static void calsubarray(int numbers[]){
        int ts=0;
        int min=0;
        int max=0;
        int sum=0;
        for(int i=0;i<numbers.length;i++){
            for(int j=i;j<numbers.length;j++){
                min=numbers[j];
                for(int k=i; k<=j; k++){

                    if(numbers[k]<min){
                    min=numbers[k];}
                    max=numbers[k];
                    if(numbers[k]>max){
                        max=numbers[k];
                    }
                    System.out.print(numbers[k]+ " ");
                }
                ts++;
                System.out.println();
                System.out.println("minimum number in the subarray is: "+ min);
                System.out.println("maximum number in the subarray is: "+ max);
            }
            max=0;

        }
            System.out.println("Total sub-arrays are: "+ ts);
            
    }

    


    public static void main(String args[]){
        int nums[]={2,88,-5,3,0};
        calsubarray1(nums);


    }
    
}
