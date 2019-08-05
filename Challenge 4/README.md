# Challenge 4 (Dynamic Programming)

## Knap Sack Problem
Given weights and values of n items, 
put these items in a knapsack of capacity C 
to get the maximum total value in the knapsack.
- *References* - Anne Spaldings CS 2.2 Lecture

### Dynamic Programming Steps taken
1. Identify the subproblems
    - Once we determine if an item should be in a Knap Sack, we check every combination of items with that and so on.
2. What does the solution roughly look like
    - The solution should return the highest value of items we can fit in our Knap Sack based on Capacity
3. Define a base case
    - The base case is if there are no items or the capacity is 0, return 0 for our value
4. Compute the value of an optimal solution (recurse and memoize)
    - Recursivly computed the values of the knap sack by comparing the maximum value to the previous value before it
    - Either adding it to the bag or not
5. Solve original problem - reconstruct from the sub-problems