public class selectionsort {
    public static void selectionsortalgo(int numbers[]){
        for(int i =0; i<numbers.length-1; i++){
            int minPosition=i;
            for(int j=i+1; j<=numbers.length-1; j++){
                if (numbers[minPosition]> numbers[j]){
                    minPosition=j;
                }
            }
            -3 6 5 0 2
            
            
            int swap = numbers[minPosition];
            numbers[minPosition]= numbers[i];
            numbers[i]=swap;
        }
    }

    public static void printArray(int numbers[]){
        for(int i=0; i<numbers.length; i++){
            System.err.print(numbers[i]+" ");
        }
        System.err.println();
    }
    public static void main(String args[]){
        int nums[]={5, 6, -3, 0, 2};
        selectionsortalgo(nums);
        printArray(nums);

        System.out.println("Hello");
    }
    
}
