# B = { x ∈ N : x^2 ≤ 16} 

# B = {1,2,3,4}

def array(x,y):
    B = []
    print("Work")
    while(x**2 <= y):
        B.append(x)
        x = x + 1
    
    print(B)

array(0,16)

array(0,100)
array(20,50)

