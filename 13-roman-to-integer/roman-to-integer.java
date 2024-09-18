class Solution {
    public int romanToInt(String s) {
        // Create a map to store the Roman numerals and their corresponding values
        Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int total = 0;  // To store the final result
        int prevValue = 0;  // To store the value of the previous Roman numeral

        // Traverse the string from left to right
        for (int i = 0; i < s.length(); i++) {
            int currentValue = romanMap.get(s.charAt(i));  // Get the value of the current Roman numeral

            // If the current value is greater than the previous value, it's a subtractive combination
            if (currentValue > prevValue) {
                // Subtract twice the previous value because it was added before
                total += currentValue - 2 * prevValue;
            } else {
                // Otherwise, just add the current value
                total += currentValue;
            }

            // Update the previous value to the current one for the next iteration
            prevValue = currentValue;
        }

        return total;
    }
}