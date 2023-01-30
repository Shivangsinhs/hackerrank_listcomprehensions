# This code generates all possible combinations of values of x, y, and z
# such that their sum is not equal to n.

if __name__ == '__main__':
    # Get input values for x, y, and z from the user
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Generate the list of lists using a list comprehension
    lis = [[i,j,k] for i in range(0,x+1) for j in range (0,y+1) for k in range (0,z+1) if(i+j+k) != n]
    
    # Print the list of combinations
    print (lis)
