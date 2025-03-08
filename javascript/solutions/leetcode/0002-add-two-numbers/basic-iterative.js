/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var resultList = null
    var sumPrevPos = null
    var carry = 0
    while (l1 || l2) {
        positionSum = carry
        if (l1) positionSum += l1.val
        if (l2) positionSum += l2.val
        carry = (positionSum > 9) ? 1 : 0
        newNode = new ListNode((positionSum > 9) ? (positionSum - 10) : positionSum)
        if (resultList) {
            sumPrevPos.next = newNode
            sumPrevPos = newNode
        } else {
            resultList = newNode
            sumPrevPos = resultList
        }
        if (l1) l1 = l1.next
        if (l2) l2 = l2.next
    }
    if (carry) sumPrevPos.next = new ListNode(1)
    return resultList
};
