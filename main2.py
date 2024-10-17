myset={1,1,2,3,3,4,5,6,7,7,8}
print(myset)
myset.add(564)
print(myset)

myset1={1,1,2,3,3,4,5,6,7,7,8}
myset2={1,8,3}

print(myset.difference(myset2))
print(myset1.symmetric_difference(myset2))
print(myset1.union(myset2))
print(myset1.intersection(myset2))

myset={"red","yellow","orange","orange","green","blue","blue","purple"}
print(myset)