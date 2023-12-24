public class insertionsort {
    public static void insertionsortalgo(int numbers[]){
        for(int i=1; i<numbers.length; i++){
            int curr=numbers[i];
            int prev=i-1;
            while(prev>=0 && numbers[prev]> curr){
                numbers[prev+1]=numbers[prev];
                prev--;
            }
            numbers[prev+1]=curr;
        }
    }
    public static void printArray(int numbers[]){
        for(int i=0; i<numbers.length; i++){
            System.err.print(numbers[i]+" ");
        }
        System.out.println();
    }
    public static void main(String args[]){
        int  nums[]={2, 1, 11, -4, 0};
        printArray(nums);
        insertionsortalgo(nums);
        printArray(nums);
    }
    
}
