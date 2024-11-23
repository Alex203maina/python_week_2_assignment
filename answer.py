
# question 1
my_list = []

# question 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# question 3
my_list.insert(2, 15)

# question 4
my_list1 = [50,60, 70]
my_list.extend(my_list1)

# question 5
my_list.remove(70)

# question 6
my_list.sort()

# question 7
index_30 = my_list.index(30)
print(index_30)

age = 0


if age >= 18:
    print("You are eligible to vote.")
else:
    print("GO HOME")