def palind(r):
    e = len(r) - 1
    s = 0
    
    while s<e :
        if(r[s] != r[e] ):
            return False
        s = s + 1
        e = e - 1
        
    return True

r = (1, 2, 3, 3, 2, 1)

if palind(r) == True:
    print("The Tuple is Flip-Flop")

else:
    print("The Tuple is not Flip_Flop")