import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
/**
 * Created by bowiehsu on 15/5/6.
 */
class ListNode{
    int val;
    ListNode next;
    ListNode(int x){val = x;}
}

//
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode record = new ListNode(0);
        ListNode tail = new ListNode(0);
        Stack<Integer> buf = new Stack<Integer>();
        record.next = head;
        tail.next = head;
        while (head != null) {
            buf.push(head.val);
            head = head.next;
        }
        //return buf;
        int lenth = buf.size();
        for (int i=0;i < lenth;i++){
            record.next.val = buf.pop();
            record = record.next;
        }
        return tail.next;
    }
}
