A={1,2,3,4,5}
B={4,5,6,7,8}


print(A|B)

C=A.union(B)
print(C)

D=B.union(A)
print(D)

#UNION
A={1,2,3,4,5}
B={4,5,6,7,8}

print(A&B)
print(A.intersection(B))
print(B.intersection(A))

print(A-B)
print(A.difference(B))
print(B-A)
print(B.difference(A))

#set symmetric difference
print(A^B)#VALUES WHICH ARE NOT COMMON IN BOTH THE SET.Therefore 4,5 excluded
print(A.symmetric_difference(B))