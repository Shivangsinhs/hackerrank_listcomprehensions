if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lis = [] # Initialize the list
    
    # Use three separate for loops to generate combinations of x, y, and z
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if (i + j + k) != n: # Check if the sum is not equal to n
                    lis.append([i,j,k]) # Add the combination to the list
    
    print(lis)
