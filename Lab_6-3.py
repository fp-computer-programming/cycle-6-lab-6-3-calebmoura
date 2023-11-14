#Author: Caleb Moura

# List of 4 colors and stored as a variable
colors = ["red", "blue", "green", "yellow"]
print("Original list of colors:", colors)

# Extend method to add 3 more colors to the list in a single statement
colors.extend(["orange", "purple", "pink"])
print("List after adding 3 colors:", colors)

# Append method to add one additional color to the list
colors.append("brown")
print("List after adding one more color:", colors)

# Insert method to insert a new color at index 3
colors.insert(3, "black")
print("List after inserting a color at index 3:", colors)

# Setting variables as equal to create a copy of the list
colors_copy = colors.copy()
print("Copy of the original list:", colors_copy)

# Remove method to remove one element from the copy of the list
removed_color = colors_copy.pop()
print(f"List after removing '{removed_color}' from the copy:", colors_copy)