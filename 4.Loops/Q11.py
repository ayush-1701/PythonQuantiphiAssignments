# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.


color_list1 = {"White", "Black", "Red", "Blue"}
color_list2 = {"Red", "Green"}

print("Result difference of colors:")
print(color_list1.difference(color_list2))