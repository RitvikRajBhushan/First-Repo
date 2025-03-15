list = [10, 25, 36, 78, 90, 45, 90]
largest = 0
second_largest= 0
for i in list:
    if i>largest:
        largest = i
for j in list:
    if j> second_largest:
        if j == largest:
            pass
        else:
            second_largest = j
print(second_largest)

