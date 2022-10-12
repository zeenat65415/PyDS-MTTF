#SET OPERATIONS-Sets acn be used to carry out mathematical set operations like union,intesection,difference and symmetric difference.

A={1,2,3,4,5}
B={4,5,6,7,8}

#Union 
print(A|B) #{1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A)) #{1, 2, 3, 4, 5, 6, 7, 8}

C=A.union(B)
print(C) #{1, 2, 3, 4, 5, 6, 7, 8}

D=B.union(A)
print(D) #{1, 2, 3, 4, 5, 6, 7, 8}


#Intersection
print(A & B) #{4,5}
print(A.intersection(B)) #{4,5}
print(B.intersection(A)) #{4,5}

#Difference
print(A-B)#elements present in A but not in B{1,2,3}
print(A.difference(B))#{1,2,3}
print(B-A)#elements present in B but not in A{8,6,7}
print(B.difference(A))#{8,6,7}

#set symmetric difference
print(A^B)#VALUES WHICH ARE NOT COMMON IN BOTH THE SET.Therefore 4,5 excluded
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))