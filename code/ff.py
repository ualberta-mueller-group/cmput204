def ff(n):
  L = [1, 6]   
  for j in range(2,n+1):    
  # j ranges from 2 to n
    L.append( L[j-2]+L[j-1] )
    # (*) invariant:  j is the index 
    # of the last element of L
  print(L[n])
