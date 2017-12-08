#aggregate and print out shopping list items

#declare list
shopping_list = list()

print("What do you want to grab from the store? ")
print("Enter DONE to stop adding items")

while True:
    new_item = input(">>> ")

    if new_item == "DONE":
        break

    shopping_list.append(new_item)

    print("You have entered {} items".format(len(shopping_list)))
    continue

print("Here is your list of items: ")

for item in shopping_list:
    print(item, ",")
