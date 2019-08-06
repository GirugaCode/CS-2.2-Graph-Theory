# Challenge 4 (Dynamic Programming)

# Knap Sack Problem
Given weights and values of n items, put these items in a knapsack of 
capacity C to get the maximum total value in the knapsack.
- *References* - Anne Spaldings CS 2.2 Lecture

### Input:
```
weight = [10, 20, 30, 15], value = [60, 100, 120, 70], capacity = 50
```
### Output:
```
The maximum value you can get is this: 230
```

### Dynamic Programming Steps taken
1. Identify the subproblems
    - Once we determine if an item should be in a Knap Sack, we check every combination of items with that and so on.
2. What does the solution roughly look like
    - The solution should return the highest value of items we can fit in our Knap Sack based on Capacity
3. Define a base case
    - The base case is if there are no items or the capacity is 0, return 0 for our value
4. Compute the value of an optimal solution (recurse and memoize)
    ```
    # Returns the maximum of two cases:
    # (1) nth item included
    # (2) not included
    return max(value[n-1] + knapSack(C-weight[n-1], weight, value, n-1), # Add it to the bag 
        knapSack(C, weight, value, n-1)) # or dont add it to the bag
    ```
5. Solve original problem - reconstruct from the sub-problems


# 42. Maximum Subarray Problem (Kadane's Algorithm)
The following folder contains both an iterative approach as well as a dynamic programming approach to this problem. 

Source: https://www.techiedelight.com/maximum-subarray-problem-kadanes-algorithm/

# Question
Given an array of integers, find the contiguous subarray within it which has the largest sum.

### Input:
```
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```
### Output:
```
[4, -1, 2, 1] // sum is 6
```

# 5 Steps of Dynamic Programming 
1. Identify the sub-problem
    1. Keeping track of the contiguous segments and to start a new one or build up on the past one
2. Guess first choice
    1. Guess the first index of the given array
3. Recursively define the value of an optimal solution
    1. 
    ```
    Let S(i) be the max sum over all contiguous subsequence ending at i

    Recurrence is defined as:

        a[i], if i = 0
        max{S(i-1) + A[i], A[i]}
    ```
4. Compute the value of an optimal solution (recurse and memoize)
    1. `@recurse`
5. Solve original problem - reconstruct from the sub-problems
    1. Sum
