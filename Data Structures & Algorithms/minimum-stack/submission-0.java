class MinStack {

    Stack<Integer> stack; 
    Stack<Integer> minStack;

    public MinStack() {
        this.stack = new Stack();
        this.minStack = new Stack();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty()) {
            minStack.push(val);
        } else {
            val = Math.min(val, minStack.peek());
            minStack.push(val);
        }
    }
    
    public void pop() {
        minStack.pop();
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
