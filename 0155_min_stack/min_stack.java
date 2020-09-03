import java.util.Stack;
import javafx.util.Pair;

class MinStack {
    private Stack<Pair<Integer, Integer>> myStack;

    /** initialize your data structure here. */
    public MinStack() {
        myStack = new Stack();
    }

    public void push(int x) {
        int tmp = myStack.isEmpty() ? x : myStack.peek().getValue();
        myStack.push(new Pair(x, Math.min(x, tmp)));
    }

    public void pop() {
        myStack.pop();
    }

    public int top() {
        return myStack.peek().getKey();
    }

    public int getMin() {
        return myStack.peek().getValue();
    }
}

/**
 * Your MinStack object will be instantiated and called as such: MinStack obj =
 * new MinStack(); obj.push(x); obj.pop(); int param_3 = obj.top(); int param_4
 * = obj.getMin();
 */