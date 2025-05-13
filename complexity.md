Big O: comparing code mathematically in terms of efficiency

Big O can measure
 - time complexity
 - space complexity

Ω - Best Case
Θ - Average Case
Ο - Worst Case (technically this is our main concern)

Rules:
 -	Drop constants (scales of n)
 - Drop smaller scale terms (drop lower degree powers)
 
O(1) ##Constant - A constant number of operations

O(log(n)) ##Divide & Conquer - 2^x=n, binary search. Splitting a sorted list in half repeatedly to locate a specific item.

O(n) ##Proportional - iterates through n parameters parameters, linear scale

O(nlog n) - most sorting algorithms

O(n^2) ##Loop within a Loop (nested)- iterates through n parameters, n*n times, quadratic scale.

O(a+b) or O(a*b) - if different variable length inputs, you cannot combine. You indicate their complexity with both variables.

Complexity for a list:

list.pop() - O(1), drop the last index and no iteration required.

list.remove(i) - O(n), need to reindex all subsequent indeces

list.insert(x,i) - O(n), need to reindex all subsequent indeces


