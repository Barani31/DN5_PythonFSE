arr = [10,20,30,40]

print("Traversal")
for x in arr:
    print(x)

arr.append(50)
print("After Insert:", arr)

arr.remove(20)
print("After Delete:", arr)