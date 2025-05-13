Linked Lists

No indeces
Non-contiguous memory

var head - first item
var tail - last item

Each node points to the next node

Append: O(1) Have tail point to a new node

Pop: O(n) Traverse from head to get n-1 node, remove pointer and assign tail to n-1 node

Prepend: O(1) Create a node, point node at head, re-assign head to new node

Dequeue: O(1) assign head to the node head points to

Remove: O(n) traverse LL, set pointer of the node before target to the node after target

Search: O(n) iterate until current == target

Node (dict):
	{
		"value": data,
		"next": node
	}