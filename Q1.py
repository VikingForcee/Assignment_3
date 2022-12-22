print("ASSIGNMENT 3")
print()
print("Q1")
print()

input_string = str(input("Enter the string:"))
list1 = input_string.split()
list2 = []


for e in list1:
    lower_e = e.lower()
    list2.append(lower_e)
set1 = set(list2)
dic = {}


for a in set1:
    count = list2.count(a)
    dic.update({a: count})
dic2 = {}
set2 = {1, 2}
set2.clear()
list3 = []


if len(list1) == 1:

    for elements in input_string:
        list3.append(elements)

    for a in list3:
        set2.add(a.lower())

    string_l = input_string.lower()
    for d in set2:
        dic2.update({d: string_l.count(d)})

    print("\n'Letter'-'Letter Count' is shown below:")
    print(dic2)

else:
    print("\n'Word'-'Word Count' is shown below:")
    print(dic)
