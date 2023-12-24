import java.util.HashSet;

class Ass1ContainDuplicates{
    public static boolean containDuplicates(int numbers[]){
        for(int i=0; i<numbers.length; i++){
            for(int j=i+1; j<numbers.length; j++){
                if(numbers[i]==numbers[j]){
                    return true;
                }
            }
        }
        return false;
    // Time complexity=O(n^2)

    }
    // Another function to calculate duplicates
    public static boolean containDuplicatesSets(int numbers[]){
        HashSet<Integer> set= new HashSet<>();  
        for (int number: numbers){
            if(!set.add(number)){
                return true;
            }
        }
        return false;
        // Space Complexity=O(n)
        // Time Complexity=O(n)
    }
    public static void main(String args[]){
        int nums[]={1,2,3,1};
        //boolean result=containDuplicates(nums);
        if(containDuplicatesSets(nums)){
            System.out.println(" The given array contains duplicates");
        }
        else{
            System.out.println(" All elements are distinct");


        }


    }
}