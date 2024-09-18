class Solution {
    public int romanToInt(String s) {
        int result = 0;

        // The Roman letter is written form largest to smallest
        // => if there is a reversion (smaller letter is written before larger) then need to do a subtraction

        // Question: will the input always be upper_case ? => handle lower case first

        // Loop through the Roman string

        s = s.toLowerCase();

        for (int i = 0; i < s.length(); i++){
            switch (s.charAt(i)){
                case 'i':
                    if ((i+1) < s.length() && (s.charAt(i+1) == 'v' || s.charAt(i+1) == 'x')){
                        result -= 1;
                    }else {
                        result += 1;
                    }
                    break;
                case 'v':
                    result += 5;
                    break;
                case 'x':
                    if ((i+1) < s.length() && (s.charAt(i+1) == 'l' || s.charAt(i+1) == 'c')){
                        result -= 10;
                    }else {
                        result += 10;
                    }
                    break;
                case 'l':
                    result += 50;
                    break;
                case 'c':
                    if ((i+1) < s.length() && (s.charAt(i+1) == 'd' || s.charAt(i+1) == 'm')){
                        result -= 100;
                    }else {
                        result += 100;
                    }
                    break;
                case 'd':
                    result += 500;
                    break;
                case 'm':
                    result += 1000;
                    break;
            }
        }

        return result;
    }
}