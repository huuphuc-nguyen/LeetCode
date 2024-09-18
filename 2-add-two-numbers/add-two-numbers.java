/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);

        ListNode currentHead = result;

        int cary = 0;

        while (l1 != null || l2 != null || cary != 0){
            int sum = cary;

            if (l1 != null){
                sum += l1.val;
                l1 = l1.next;

            }

            if (l2 != null){
                sum += l2.val;
                l2 = l2.next;

            }

            cary = sum / 10;

            sum = sum % 10;

            ListNode newNode = new ListNode(sum);
           currentHead.next = newNode;
            currentHead = currentHead.next;
        }

        return result.next;
    }
}