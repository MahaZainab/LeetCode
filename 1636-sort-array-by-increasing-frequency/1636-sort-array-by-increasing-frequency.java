class Solution {
    public int[] frequencySort(int[] nums) {
             // Step 1: Count the frequency of each element
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Step 2: Convert the array to a list of integers
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }

        // Step 3: Sort the list using a custom comparator
        Collections.sort(list, (a, b) -> {
            int freqA = frequencyMap.get(a);
            int freqB = frequencyMap.get(b);
            if (freqA != freqB) {
                return freqA - freqB; // Sort by frequency (ascending)
            } else {
                return b - a; // Sort by value (descending)
            }
        });

        // Step 4: Convert the list back to an array
        for (int i = 0; i < list.size(); i++) {
            nums[i] = list.get(i);
        }

        return nums;
        
    }
}