
class Solution {
    public String decodeString(String s) {
        StringBuilder result = new StringBuilder(); 
        result.append(s); 
        StringBuilder subString = new StringBuilder();  
        int k = 0;  
        Stack<Integer> countStack = new Stack<>();
        Stack<StringBuilder> stringStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {

            if (Character.isDigit(s.charAt(i))){
                k = k*10 + (s.charAt(i) - '0');
            }
            else if (s.charAt(i) == '['){
                countStack.push(k);
                stringStack.push(subString);
                subString = new StringBuilder();
                k = 0;
            }
            else if (s.charAt(i) == ']'){
                int repeat = countStack.pop();
                result = stringStack.pop();
                for (int j = 0; j < repeat; j++) {
                    result.append(subString.toString());
                }
                subString = result;
                if (!countStack.isEmpty()){
                    result = new StringBuilder();

                }
            }
            else {
                subString.append(s.charAt(i));
            }
        }

        return result.toString();
}
}