public class bubblesort {
    public static void calbubblesort(int number[]){
        for(int turn=0; turn<number.length-1; turn++){
            for (int j=0; j<number.length-1-turn; j++){
                if(number[j]> number[j+1]){
                    int swap=number[j];
                    number[j]=number[j+1];
                    number[j+1]= swap;
                }
            }
        }
    }

    public static void bubblesortalgo(int numbers[]){
        for(int turn=0; turn<numbers.length-1; turn++){
            for( int j=0; j<numbers.length-1-turn; j++ ){
                if(numbers[j]>numbers[j+1]){
                    int swap= numbers[j];
                    numbers[j]=numbers[j+1];
                    numbers[j+1]=swap;
                }
            }
        }
    }
    public static void printarray(int numbers[]){
        for(int i=0; i<numbers.length; i++){
            System.err.print(numbers[i]+ " ");
        }
        System.out.println();
    }
    public static void main(String args[]){
        int  nums[]={5,9,8,4,1};
        System.err.println("Array before sorting");
        printarray(nums);
        bubblesortalgo(nums);
        System.err.println("Array after sorting");
        printarray(nums);

    }
}
