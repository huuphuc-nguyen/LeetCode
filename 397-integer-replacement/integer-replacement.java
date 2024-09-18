class Solution {

    private Map<Long, Integer> memo = new HashMap<>();

    private int integerReplacement(long n){
        if (n == 1) return 0;

        if (memo.containsKey(n))
            return memo.get(n);

        int result;
        if (n % 2 == 0) {
            result = 1 + integerReplacement(n / 2);
        } else {
            result = 1 + Math.min(integerReplacement(n + 1), integerReplacement(n - 1));
        }

        memo.put(n, result);
        return result;
    }

    public int integerReplacement(int n) {
        return integerReplacement((long) n);
    }
}