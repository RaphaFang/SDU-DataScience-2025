package ds_and_alg.adt;

// -------------------------------------------------------
// ! (1.6) Priority Queue
// -------------------------------------------------------
import java.util.PriorityQueue;
import java.util.Comparator;

class Task {
    String name;
    int priority;

    public Task(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    @Override
    public String toString() {
        return name + "(" + priority + ")";
    }
}

class TaskScheduler {
    public static void main(String[] args) {
        // priority 小的先出隊（min-heap 行為）
        PriorityQueue<Task> queue = new PriorityQueue<>(Comparator.comparingInt(t -> t.priority));
        // 如果要大的優先
        // PriorityQueue<Task> queue = new PriorityQueue<>(Comparator.comparingInt(t ->
        // t.priority).reversed());

        queue.offer(new Task("Clean", 3));
        queue.offer(new Task("Eat", 1));
        queue.offer(new Task("Study", 2));

        System.out.println(queue.poll()); // Eat(1)
        System.out.println(queue.poll()); // Study(2)
        System.out.println(queue.poll()); // Clean(3)
    }
}
