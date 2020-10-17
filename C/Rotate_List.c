/*
https://leetcode.com/problems/rotate-list/submissions/
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode *rotateRight(struct ListNode *head, int k) {
    if (!head || k == 0) return head;

/*
Used to count the size of the array.
*/
	struct ListNode* lastNode = head;
	int n = 1;
	while (lastNode->next)
	{
		lastNode = lastNode->next;
		n++;
	}

/*
Used to remove any complete rotations from the list.
Example: If size of list is n, and no. of rotations = k
if (n==k)
then no rotations is required.
so n = n%k removes all complete roations.
*/
	k = k%n;
	if (k == 0) return head;
	k = n - k;

	lastNode->next = head;
	struct ListNode *newHead = head;

	for (int i = 0; i < k - 1; i++)
		newHead = newHead->next;

	head = newHead->next;
	newHead->next = NULL;
	return head;
}
