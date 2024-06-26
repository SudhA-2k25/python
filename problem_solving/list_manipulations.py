#Find the maximum and minimum values in the list.
#Calculate the sum of all elements in the list.
#Sort the list in ascending order.
#Remove duplicate elements from the list

def list_op(lst):
    max_val = max(lst)
    min_val = min(lst)

    sum_of_elements = sum(lst)

    sorted_list = sorted(lst) # Asc order
    desc_order = sorted(lst , reverse = True)

    unique_elements = list(set(lst))  # unique elements

    return max_val , min_val , sum_of_elements , sorted_list ,desc_order , unique_elements

print(list_op([4,5,6,7,8,10,12]))
# or
obj = list_op([4,5,6,7,8,10,12])

print(f"maximum value = {obj[0]}")
print(f"minimum value = {obj[1]}")
print(f"sum = {obj[2]}")
print(f"sorted list = {obj[3]}")
print(f"descendinglist = {obj[4]}")
print(f"unique elements = {obj[5]}")
