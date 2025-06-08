package ds_and_alg;

import java.util.Deque;
import java.util.ArrayDeque;

public class UndoRedo {

    private Deque<String> undoStack = new ArrayDeque<>();
    private Deque<String> redoStack = new ArrayDeque<>();

    public void type(String text) {
        undoStack.push(text);
        redoStack.clear();
    }

    public String undo() {
        if (!undoStack.isEmpty()) {
            String action = undoStack.pop();
            redoStack.push(action);
            return "Undo: " + action;
        }
        return "Nothing to undo.";
    }

    public String redo() {
        if (!redoStack.isEmpty()) {
            String action = redoStack.removeFirst();
            undoStack.addLast(action);
            return "Redo: " + action;
        }
        return "Nothing to redo.";
    }

    public String printState() {
        return "Current: " + undoStack;
    }

    public static void main(String[] args) {
        UndoRedo editor = new UndoRedo();
        editor.type("A");
        editor.type("B");
        System.out.println(editor.undo()); // Undo: B
        System.out.println(editor.redo()); // Redo: B
        System.out.println(editor.printState()); // [B, A]
    }
}
