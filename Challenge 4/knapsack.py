"""
Given weights and values of n items, 
put these items in a knapsack of capacity C 
to get the maximum total value in the knapsack.

NOTE: This challenge was done by Ryan Nguyen and Tim Kaing
"""
def knapSack(C, weight, value, n):
    """
    Params:
    C -> The capacity weight of items we are able to hold
    weight -> How heavy a certain item is
    value -> The value of a certain item
    n -> number of items to consider
    """
    # n = len(value) -1

    # Base Case
    if n == 0 or C == 0:
        return 0 

    # If weight of the nth item is more the C(capacity of knapsack),
    # then the item cannot be in the optimal solution
    # Crosses it out of the tree
    if weight[n-1] > C:
        return knapSack(C, weight, value, n-1)

    # Returns the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(value[n-1] + knapSack(C-weight[n-1], weight, value, n-1), # Add it to the bag 
        knapSack(C, weight, value, n-1)) # or dont add it to the bag

if __name__ == "__main__":
    # To test above function 
    weight = [10, 20, 30, 15]
    value = [60, 100, 120, 70]
    C = 50
    n = len(value)
    # print(knapSack(C , weight , value , n))

    print("For this input:")
    print("List of items with weight and value:")
    print(list(zip(weight, value)))
    print(f"Size of knapsack: {C}\n")

    print("The maximum value you can get is this:")
    print(knapSack(C, weight, value, n))