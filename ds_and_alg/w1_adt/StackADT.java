package ds_and_alg.adt;

import java.util.Stack;
import java.util.Deque;
import java.util.ArrayDeque;

// -------------------------------------------------------
// ! (1.2) Stack, LIFO
// -------------------------------------------------------
public class StackADT {
    public static boolean StackADT(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    static boolean DequeADT(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        // with Stack & Stack
        System.out.println(StackADT("((()))"));
        System.out.println(StackADT("(()"));

        // with deque & ArrayDeque<>
        System.out.println(DequeADT("(()())"));
        System.out.println(DequeADT("(()"));
    }
}
