class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        for (char c : s.toCharArray()) {
            if (!map.containsKey(c)) {
                stack.push(c);
                continue;
            }
            if (stack.isEmpty() || stack.peek() != map.get(c)) {
                return false;
            }
            stack.pop();
        }
        return stack.isEmpty();

    }
}
