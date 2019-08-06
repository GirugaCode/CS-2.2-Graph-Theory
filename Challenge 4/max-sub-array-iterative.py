from sys import maxsize

def max_sub_array(a, size):
    # stores current maximum sum of sub-array found so far
    max_so_far = -maxsize - 1
    # stores current maximum sum of sub-array that ends at current position
    max_ending_here = 0
    
    # keeps track of the indices
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    
    print ("Maximum contiguous sum is: ", (max_so_far)) 
    print ("Maximum contiguous subarray: ", a[start:end+1]) 

if __name__ == "__main__": 
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    max_sub_array(a,len(a)) 
