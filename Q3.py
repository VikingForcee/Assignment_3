print("Q3")
print()

list1 = list(map(int, input("Enter the numbers separated by space:").split()))

list2 = []
for a in list1:
    t = (a, a * a)
    list2.append(t)

print("\nList containing (n,n^2) is shown below:")
print(list2)
