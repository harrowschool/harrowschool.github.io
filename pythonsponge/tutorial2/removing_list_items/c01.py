furniture = ['chair', 'bed', 'sofa', 'chair']

# remove the sofa (from index 2) and store it in the variable item
item = furniture.pop(2)
print("we took out the", item, "and now the list is", furniture)

# only the first chair will be removed here
furniture.remove("chair")
print("we took out the first chair and now the list is", furniture)
