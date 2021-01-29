// https://binarysearch.com/problems/Linked-List-Deletion
// Explanation: https://stackoverflow.com/questions/12914917/using-pointers-to-remove-item-from-singly-linked-list

/**
 * class LLNode {
 *     public:
 *         int val;
 *         LLNode *next;
 * };
 */
LLNode* solve(LLNode* node, int target) {
    LLNode** pp = &node;
    while (*pp != nullptr) {
        if ((*pp)->val == target) {
            *pp = (*pp)->next;
        } else {
            pp = &(*pp)->next;
        }
    }
    return node;
}