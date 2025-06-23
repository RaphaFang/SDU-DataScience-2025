package ds_and_alg.adt;

// -------------------------------------------------------
// ! (1.4) Queue(舊方法) vs Deque, FIFO
// -------------------------------------------------------
import java.util.Queue;
import java.util.ArrayDeque;

public class QueueADT {
    private Queue<String> queue;

    public QueueADT() {
        this.queue = new ArrayDeque<>();
    }

    public void enqueue(String name) {
        queue.offer(name);
    }

    public String dequeue() {
        return queue.poll();
    }

    public String peek() {
        return queue.peek();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public static void main(String[] args) {
        QueueADT cq = new QueueADT();
        cq.enqueue("Charlie");
        cq.enqueue("Dana");
        System.out.println(cq.peek()); // Charlie
        System.out.println(cq.dequeue()); // Charlie
        System.out.println(cq.dequeue()); // Dana
        System.out.println(cq.isEmpty()); // true
    }
}
// "ArrayDeque is likely to be faster than Stack when used as a stack, and
// faster than LinkedList when used as a queue."