import java.util.List;

/**
 * Created by bowiehsu on 15/5/9.
 */
public class Main {

    public static void main(String[] args){
        Solution instance = new Solution();
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        node1.next = node2;
        ListNode res = instance.reverseList(node1);
        while (res != null) {
            System.out.print(res.val);
            res = res.next;
        }
    }
}
